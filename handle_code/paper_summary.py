import shutil
import os
from io import BytesIO
import subprocess
import time
from pathlib import Path
import datetime
import json
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def read_hf_paper_html(url, file_name):
    """
    Reads the HTML of a paper from the HuggingFace website.
    """
    response = requests.get(url)
    html_content = response.text
    # Save the HTML content to a local file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

def parse_html(html_file):
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()
    # Create a BeautifulSoup object and parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")
    a_tags = soup.find_all("a")
    paper_titles_and_links = []

    for tag in a_tags:
        title = tag.get_text(strip=True)
        link = tag.get("href")
        if title and link:
            paper_titles_and_links.append({"title": title, "link": link})
    # 过滤无效内容
    paper_item = []
    for item in paper_titles_and_links:
        if '/papers/2' in item['link'] and  len(item['title']) > 15:
            paper_item.append(item)
    for item in paper_item:
        link = item['link']
        arxiv_id = link.split('/')[-1]
        arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
        arxiv_pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
        item['arxiv_pdf_url'] = arxiv_pdf_url
        item['arxiv_url'] = arxiv_url
        item['arxiv_id'] = arxiv_id
    return paper_item

def download_pdf(url, path, local_filename=None):
    """
    下载指定URL的PDF文件并保存到本地。
    
    :param url: PDF文件的网址
    :param local_filename: 本地保存的文件名，默认为None则使用URL的最后一部分作为文件名
    """
    # 发送HTTP GET请求获取PDF文件内容
    response = requests.get(url, stream=True)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 如果未指定本地文件名，则从URL中提取
        if not local_filename:
            content_disposition = response.headers.get('content-disposition')
            if content_disposition:
                filename = content_disposition.split("filename=")[-1]
                local_filename = filename.strip("\"'")
            else:
                local_filename = url.split("/")[-1]
        
        # 使用BytesIO处理二进制数据，避免大文件内存问题
        with BytesIO(response.content) as pdf_buffer:
            # 使用shutil将BytesIO对象的内容写入本地文件
            with open(os.path.join(path, local_filename), 'wb') as f:
                shutil.copyfileobj(pdf_buffer, f)
        
        print(f"PDF文件已成功保存为: {local_filename}")
    else:
        print(f"请求失败，状态码：{response.status_code}")
    return os.path.join(path, local_filename)

def summary_paper(paper_path, prompt):
    client = OpenAI(
    api_key="sk-d71e4818164d4813b6fe6c9f70c2e745",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    file_object = client.files.create(file=Path(paper_path), purpose="file-extract")
    print(f'{paper_path} create finish: {file_object}')
    completion = client.chat.completions.create(
    model="qwen-long",
    messages=[
        {
            'role': 'system',
            'content': prompt,
        },
        {
            'role': 'system',
            'content': f'fileid://{file_object.id}'
        },
        {
            'role': 'user',
            'content': '请总结：'
        }
    ],
    stream=True
    )
    content = []
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content.append(chunk.choices[0].delta.content)
            # print(chunk.choices[0].dict())
    return ''.join(content)

def summary_paper_with_data(data, prompt):
    today_str = data
    folder_name = f"{today_str}"
    hf_url = f'https://huggingface.co/papers?date={today_str}'
    hf_html_file_name = 'huggingface_papers.html'
    paper_info_file_name = f'paper_read/{today_str}_paper_info.json'
    summary_info_file_name = f'paper_read/{today_str}_summary_info.md'

    def init_env(folder_name):
        # 创建一个文件夹使用today_date作为文件夹名称
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    init_env(folder_name)
    # 分析dailay 网站获取论文和url
    read_hf_paper_html(hf_url, hf_html_file_name)
    paper_info = parse_html(hf_html_file_name)

    def save_to_json(data, json_file):
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
    save_to_json(paper_info, paper_info_file_name)

    # 进行总结
    def summary_paper_retry(file_path, retry=10):
        for i in range(retry):
            try:
                summary_info = summary_paper(file_path, prompt)
                return summary_info
            except Exception as e:
                print(f"summary_paper_retry error: {e}")
                time.sleep(10)

        return '# faild to  read !!!!'

    for paper in tqdm(paper_info):
        file_path = download_pdf(paper['arxiv_pdf_url'], folder_name)
        summary_info = summary_paper_retry(file_path)
        with open(summary_info_file_name, 'a', encoding='utf-8') as file:
            file.write("\n")
            file.write(f'# {paper["title"]}\n')
            file.write(f'[arxiv_pdf_url]({paper["arxiv_pdf_url"]})\n')

            file.write(summary_info)

def upload_file(data):
    now_path = os.getcwd()
    directory_path = "/root/meta_gpt/hf_paper_summary/paper_read"
    # 改变当前工作目录
    os.chdir(directory_path)

    command = "git add ."  # 对于Unix/Linux
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
    command = f'git commit -m "paper summary {data}"'  # 对于Unix/Linux
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
    command = f'git push'  # 对于Unix/Linux
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
    os.chdir(now_path)
# 获取前一天的日期
def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday

    is_saturday = yesterday.weekday() == 5
    is_sunday = yesterday.weekday() == 6
    return yesterday.strftime("%Y-%m-%d"), is_saturday or is_sunday
prompt1 = '''请阅读以下论文，并提供一个详细的中文总结，包括以下要点：
论文标题
研究的主要目标和问题
使用的方法和技术
实验设计和主要结果
研究的结论和对未来工作的影响
任何重要的图表或数据点
请确保总结是准确、清晰，并且专业。总结的长度应不超过500字，使用markdown格式输出。'''

prompt2 = '''
请仔细阅读论文，并依据下列结构撰写一份详尽的中文摘要，总字数控制在500字以内，采用markdown格式输出：
1. **论文标题**  
   - 请在此处插入论文标题的中文翻译。
2. **作者信息**  
   - 列出论文的所有作者姓名和机构。
3. **论文标签**  
   - 精确描述论文的主题分类或关键词。
4. **研究核心目标与问题**  
   - 概括研究旨在解决的核心问题及研究的重要性。
5. **采用方法与技术**  
   - 详细说明研究中应用的主要方法、算法、模型或其他关键技术手段。
6. **实验设计与主要发现**  
   - 描述实验的设计框架，包括样本选择、实验分组、控制变量等，并总结最重要的实验结果。
7. **结论及对未来研究的意义**  
   - 总结研究的主要结论及其对领域内未来研究方向的潜在影响。
8. **关键图表与数据**  
   - 简要提及对理解研究结果至关重要的图表、数据点或统计分析结果。
请确保摘要内容准确无误，表述清晰且符合专业标准。
'''

if __name__ == '__main__':
    # today_str, is_weekend = get_yesterday()
    # if is_weekend:
    #     print(f'{today_str} is weekend, skip')
    #     exit(0)
    # print(f'{today_str} start summary')
    # today_str='2024-07-01'
    today_str='2024-07-02'
    days = ['2024-07-24', '2024-07-25', '2024-07-26', '2024-07-29']
    for day in days:
        summary_paper_with_data(day, prompt2)
        upload_file(day)

