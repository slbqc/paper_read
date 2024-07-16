
#   Summary of a Haystack: A Challenge to Long-Context LLMs and RAG Systems
1. **论文标题**  
   - Summary of a Haystack: A Challenge to Long-Context LLMs and RAG Systems

2. **作者信息**  
   - Philippe Laban, Alexander R. Fabbri, Caiming Xiong, Chien-Sheng Wu
   - Salesforce AI Research

3. **论文标签**  
   - 大型语言模型(LLMs)
   - 检索增强生成系统(RAG)
   - 长文本处理
   - 文本摘要
   - 评估方法

4. **研究核心目标与问题**  
   - 研究旨在通过提出一种新的评价基准“Summary of a Haystack”(SummHay)，来评估长文本上下文处理能力。当前的大型语言模型(LLMs)和检索增强生成系统(RAG)虽然能处理大量输入，但对其输出质量的评估仍然存在挑战。传统任务如寻找针头在干草堆中的位置缺乏复杂度，无法充分测试这些系统的性能。

5. **采用方法与技术**  
   - 该工作设计了一种合成干草堆文档集合的方法，确保特定见解在文档中重复出现。SummHay任务要求系统处理干草堆并根据查询生成摘要，同时准确引用源文档。通过已知的应出现在摘要中的见解和应该被引用的文档，实现了可高度复现的自动评估，包括覆盖率和引用两个方面。

6. **实验设计与主要发现**  
   - 实验在对话和新闻两个领域生成了干草堆，对10个LLMs和相应的50个RAG系统进行了大规模评估。结果显示，即使是拥有文档相关性Oracle信号的系统，其综合得分也比估计的人类表现低10多分。没有检索器的长文本LLMs，如GPT-4o和Claude 3 Opus，在SummHay上的得分低于20%。

7. **结论及对未来研究的意义**  
   - 结论表明，SummHay对当前系统而言是一个开放性的挑战。研究希望未来的系统能在SummHay上达到甚至超越人类的表现，从而提供更可靠和值得信赖的答案引擎。此外，SummHay也可用于研究企业级RAG系统和长文本模型中的位置偏置问题。

8. **关键图表与数据**  
   - 论文中报告了所有系统在SummHay基准上的精度、召回率以及F1分数(引用得分)，揭示了不同系统在精确性和全面性之间的平衡情况。例如，Claude 3 Sonnet的引用精度为67.3%，召回率为42.2%，F1分数为51.7%。而人类表现的F1分数达到了76.7%。
#   OpenVid-1M: A Large-Scale High-Quality Dataset for Text-to-video Generation
1. **论文标题**  
   - 大规模高质量文本到视频生成数据集OpenVid-1M

2. **作者信息**  
   - 南京大学的Kepan Nan、Rui Xie、Jian Yang、Ying Tai；  
   - 字节跳动的Penghao Zhou、Zhenheng Yang、Zhijie Chen；  
   - 南开大学的Xiang Li。

3. **论文标签**  
   - 文本到视频生成、多模态模型、视频扩散变换器、高质量数据集、高分辨率视频生成

4. **研究核心目标与问题**  
   - 解决文本到视频生成领域缺乏精确高质量公开数据集的问题，以及现有方法未能充分利用文本信息进行视频生成的不足。

5. **采用方法与技术**  
   - 构建了一个包含超过1百万个视频片段的大规模数据集OpenVid-1M，这些片段具有高美学价值、清晰度和表达力丰富的文本描述。
   - 设计了一个自动化数据处理管道，以筛选出具备高审美性、时间一致性、流畅运动和清晰度的视频。
   - 提出了Multi-modal Video Diffusion Transformer (MVDiT)，能够同时挖掘视觉令牌的结构信息和文本令牌的语义信息。

6. **实验设计与主要发现**  
   - 使用700个提示词生成视频并采用一系列指标评估生成质量，实验结果表明，该团队的方法在多项指标上优于现有技术，尤其是在视频美学和清晰度方面。
   - 通过消融研究验证了不同分辨率、模型架构和训练数据量对性能的影响，以及数据处理步骤的有效性。

7. **结论及对未来研究的意义**  
   - OpenVid-1M数据集和MVDiT模型为文本到视频生成领域的研究提供了新的工具，其高质量的视频生成能力将推动这一领域的发展。

8. **关键图表与数据**  
   - 表格展示了与其他SOTA模型的量化比较，突出了OpenVid-1M和MVDiT的优越性。
   - 图表直观呈现了模型在不同任务上的表现，如视频清晰度和对文本提示的理解能力。
#   Agentless: Demystifying LLM-based Software Engineering Agents
1. **论文标题**  
   - 《AGENTLESS: 大型语言模型驱动软件工程代理的迷思》

2. **作者信息**  
   - Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang
   - University of Illinois Urbana-Champaign

3. **论文标签**  
   - 大型语言模型(LLMs)、软件开发自动化、代码生成、程序修复、测试生成、自主软件代理

4. **研究核心目标与问题**  
   - 鉴于大型语言模型(LLMs)在代码合成、程序修复和测试生成任务中的显著进步，本研究旨在评估是否真的需要复杂的自主软件代理来执行端到端的软件开发。研究聚焦于现有LLM代理的复杂性和当前LLMs的能力限制，提出了一个无需代理的解决方案。

5. **采用方法与技术**  
   - 构建了一个名为AGENTLESS的无代理方法，该方法使用两阶段过程：定位问题后进行修复，不依赖LLM决定未来行动或操作复杂工具。这种方法比基于代理的方法更简单直接。

6. **实验设计与主要发现**  
   - 在流行的SWE-bench Lite基准上进行了测试，结果显示AGENTLESS不仅性能最高(27.33%)，而且成本最低($0.34)，超越所有已知开源软件代理。手动分析了SWE-bench Lite中的问题，识别出具有精确补丁或问题描述不足/误导性的问题。基于此构建了SWE-bench Lite-S，排除了问题描述不当的任务，以进行更严格的评估。

7. **结论及对未来研究的意义**  
   - 研究突显了简单、可解释的技术在自主软件开发领域的潜力。AGENTLESS有望为自主软件开发的基线、起点和未来方向设定新的标准，促进领域内的进一步发展。

8. **关键图表与数据**  
   - 图5展示了SWE-bench Lite问题的分类和细分，包括描述质量、解决方案在描述中的存在、位置信息等维度的分布情况。图6比较了不同方法在SWE-bench Lite-S不同问题类别上的解决率，显示了有无示例代码、解决方案步骤和位置信息对解决问题的影响。
#   MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention
1. **论文标题**  
   - MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention

2. **作者信息**  
   - Huiqiang Jiang, Yucheng Li, Chengruidong Zhang, Qianhui Wu, Xufang Luo, Surin Ahn, Zhenhua Han, Amir H. Abdi, Dongsheng Li, Chin-Yew Lin, Yuqing Yang, Lili Qiu  
   - 机构：Microsoft Corporation, University of Surrey  
   - 邮箱：{hjiang,chengzhang,yuqyang}@microsoft.com, yucheng.li@surrey.ac.uk

3. **论文标签**  
   - 大型语言模型, 长序列处理, 动态稀疏注意力, 高性能计算

4. **研究核心目标与问题**  
   - 论文针对大型语言模型（LLM）推理过程中计算挑战这一核心问题，特别是随着提示长度增加带来的显著延迟。研究旨在加速长上下文LLM的预填充阶段，以降低延迟并提高效率。

5. **采用方法与技术**  
   - 引入MInference，一种专为加速长序列处理设计的稀疏计算方法。该方法识别并利用长上下文注意力矩阵中的三种独特模式——A形、垂直斜杠和块稀疏模式——来优化GPU上的稀疏计算。通过离线确定每个注意力头的最佳模式，并在推理时动态构建稀疏索引，MInference实现高效稀疏注意力计算，大幅减少长上下文LLM预填充阶段的延迟。

6. **实验设计与主要发现**  
   - 在一系列下游任务上评估MInference，包括InfiniteBench、RULER、PG-19和Needle In A Haystack，以及多种模型如LLaMA-3-1M、GLM-4-1M、Yi-200K、Phi-3-128K和Qwen2-128K。结果表明，MInference能有效将预填充阶段的推理延迟减少至多10倍。

7. **结论及对未来研究的意义**  
   - MInference通过动态稀疏注意力计算显著提升了长上下文LLM的推理速度，无需修改预训练设置或额外微调。它在生成高质量、类人总结和精确的键值对检索任务上表现出优越性，对于促进长上下文LLM的广泛应用和AI民主化具有重要意义。

8. **关键图表与数据**  
   - 图13展示了使用Flan-UL2在Summarization数据集上T5风格编码器注意力的稀疏模式。表8比较了不同方法在EN.SUM任务上的生成性能，基于LLaMA-3-8B-262K模型；表9则展示了Retrieve.KV任务上各种方法的表现。这些图表和数据点证实了MInference在保持高精度的同时，实现了显著的性能提升。
#   Understanding Alignment in Multimodal LLMs: A Comprehensive Study
1. **论文标题**  
   - 《理解多模态LLM中的对齐：一项全面研究》

2. **作者信息**  
   - Elmira Amirloo, Jean-Philippe Fauconnier, Christoph Roesmann, Christian Kerl, Rinu Boney, Yusu Qian, Zirui Wang, Afshin Dehghan, Yinfei Yang, Zhe Gan, Peter Grasch
   - 机构: Apple Inc.

3. **论文标签**  
   - 大型语言模型(LLM), 多模态大型语言模型(MLLM), 对齐, 厅想, 强化学习, 数据集构造

4. **研究核心目标与问题**  
   - 研究旨在探索和理解多模态大型语言模型(MLLM)中偏好对齐的重要性和影响，尤其是如何通过不同的对齐策略来减少模型产生的厅想(不准确或与图像内容不符的响应)。

5. **采用方法与技术**  
   - 论文将对齐算法分为离线(如直接偏好优化(DPO))和在线(如在线-DPO)两大类，并探讨结合使用两种方法的可能性。引入了一种名为“偏差驱动的厅想采样”(BDHS)的新方法，该方法不需要额外的标注或外部模型即可生成有效的偏好数据。

6. **实验设计与主要发现**  
   - 实验部分评估了不同对齐方法的效果，包括强化学习(RL)技术、在线和混合DPO策略以及各种离线方法。对比了多个公开的偏好数据集，强调了高质量偏好数据集的标准。研究发现，BDHS能够遵循这些最佳实践，提供简单而有效的方法，其性能与先前发表的多模态模型对齐工作相当。

7. **结论及对未来研究的意义**  
   - 结论表明，通过特定的对齐策略，如结合离线和在线方法，可以显著提升MLLM的性能。此外，BDHS作为一种创新的数据创建方式，无需额外资源即可提高模型对视觉信息的忠实度。这些发现为未来的多模态模型训练提供了新的视角和实践指导。

8. **关键图表与数据**  
   - 图表显示了偏好数据集大小对模型性能的影响，其中BDHS在某些指标上表现出色，例如在LLaVA-in-the-Wild和MMHALBench上的厅想率。实验还展示了不同迭代下BDHS变体的响应生成过程，揭示了指导自由响应生成的特性。
#   To Forget or Not? Towards Practical Knowledge Unlearning for Large Language Models
**论文标题**
   - 大型语言模型中的实用知识遗忘：走向精确的知识卸载

**作者信息**
   - Tian, Bozhong, Liang, Xiaozhuan, Cheng, Siyuan, Liu, Qingbin, Wang, Mengru, Sui, Dianbo, Chen, Xi, Chen, Huajun, Zhang, Ningyu
   - 浙江大学, 腾讯平台与内容集团, 哈尔滨工业大学

**论文标签**
   - 大型语言模型, 知识卸载, 隐私保护, 版权法, 训练效率

**研究核心目标与问题**
   - 本研究旨在解决大型语言模型(LLMs)在训练过程中不可避免地保留敏感数据的问题，如个人隐私和版权材料，这威胁到系统的安全性和完整性。研究聚焦于开发一种更精准的方法来卸载这些敏感知识，同时尽量减少对模型一般知识的损害。

**采用方法与技术**
   - 研究引入了一个基准KnowUnDo，包含版权内容和用户隐私领域，用于评估LLMs在知识卸载过程中的表现，尤其是检查是否错误地删除了重要知识。提出了MemFlex方法，通过利用梯度信息精确定位并卸载敏感参数，以避免过度卸载。

**实验设计与主要发现**
   - 实验设计包括使用Qwen-1.5-7B-Chat模型进行用户隐私领域的知识卸载测试。结果显示，现有卸载方法往往导致过度卸载，而MemFlex方法在精确卸载特定知识的同时，能更好地保持模型的一般知识。在对比实验中，MemFlex方法在卸载时间、GPU资源消耗上也优于其他基线方法。

**结论及对未来研究的意义**
   - 研究证实MemFlex在大型语言模型的知识卸载方面表现出色，不仅能够有效卸载敏感知识，还能最大限度地保留模型的一般能力。这为今后开发更安全、更合规的LLMs提供了新的方向，特别是在处理敏感数据和遵守隐私法规方面。

**关键图表与数据**
   - 表4展示了在用户隐私领域卸载Qwen-1.5-7B-Chat模型的整体结果，MemFlex方法在卸载成功率达到89.36%，保留成功率78.17%，平均性能83.76%，优于其他方法。表5比较了所有基线和MemFlex方法在LLaMA模型上的训练时间和GPU VRAM使用情况，MemFlex在效率上同样领先。
#   Consistency Flow Matching: Defining Straight Flows with Velocity Consistency
**论文标题**
   - 一致性流匹配：通过速度一致性定义直线流

**作者信息**
   - Ling Yang, Zixiang Zhang, Zhilong Zhang, Xingchao Liu, Minkai Xu, Wentao Zhang, Chenlin Meng, Stefano Ermon, Bin Cui
   - 作者分别来自北京大学、德克萨斯大学奥斯汀分校、斯坦福大学和Pika Labs

**论文标签**
   - 流匹配、深度生成模型、概率路径、普通微分方程、一致性约束

**研究核心目标与问题**
   - 本研究旨在提出一种名为一致性流匹配(Consistency-FM)的新方法，该方法通过在流的速度场空间中强制执行自一致性来优化流匹配框架。目的是为了减少采样时的函数评估次数并提高图像生成的质量。

**采用方法与技术**
   - 研究中使用了一种新的流匹配方法，它直接从不同的时间点定义直线流到同一终点，同时在速度值上施加约束以确保流的一致性。此外，引入了多段训练策略来增强表达能力，实现样本质量和速度之间的更好折衷。

**实验设计与主要发现**
   - 实验在CIFAR-10、CelebA-HQ和AFHQ-Cat三个经典图像数据集上进行。结果显示，Consistency-FM比一致性模型快4.4倍，比修正流模型快1.7倍，同时生成样本的质量更优。实验还表明，在高分辨率图像生成任务中，Consistency-FM相对于现有最佳方法有显著提升，尤其是在收敛速度和生成图像的逼真度方面。

**结论及对未来研究的意义**
   - 研究证明了Consistency-FM在训练效率和生成质量方面的优越性，特别是在处理复杂数据分布和高分辨率图像时。这为未来的深度生成模型提供了一个更高效、更精确的采样方案。

**关键图表与数据**
   - 图2展示了与传统流匹配、一致性模型和一致性轨迹模型相比，Consistency-FM在训练和采样过程中如何通过定义直线流来减轻离散化错误和近似误差。
   - 表格数据显示了在不同数据集上Consistency-FM与现有模型的比较，特别是在NFE(函数评估次数)和FID分数(生成图像质量度量)上的表现。
#   Magic Insert: Style-Aware Drag-and-Drop
# faild to  read !!!!
#   Revealing Fine-Grained Values and Opinions in Large Language Models
**论文标题**
揭示大型语言模型中的细粒度价值观与意见

**作者信息**
Dustin Wright*, Arnav Arora*, Nadav Borenstein, Srishti Yadav, Serge Belongie, Isabelle Augenstein
大学哥本哈根&先锋AI中心
{dw, aar, nb, srya, s.belongie, augenstein}@di.ku.dk

**论文标签**
大型语言模型(LLMs), 偏见识别, 道德与政治立场, 文本分析, 细粒度价值观

**研究核心目标与问题**
研究旨在揭示大型语言模型(LLMs)中的潜在价值观与意见，以识别偏见并减轻可能造成的伤害。通过分析LLMs对道德和政治陈述的态度，可以了解模型如何影响用户观点，以及它们可能具有的潜在说服力。

**采用方法与技术**
本研究分析了一个包含156,000个由6个LLMs生成的对政治罗盘测试(PCT)62个命题的响应的大规模数据集，使用了420种不同的提示变化。研究不仅进行了粗粒度的立场分析，还提出了细粒度分析方法，通过识别“trope”——语义上相似且在不同提示下一致出现的短语模式，来深入理解模型生成文本背后的模式。

**实验设计与主要发现**
研究通过向模型提供PCT中的命题并收集其响应，观察到模型的立场会因提示方式的不同而显著变化。发现添加到提示中的人口统计特征对PCT的结果有重大影响，反映出模型的偏见；同时，当要求模型生成封闭式或开放式领域响应时，结果也存在差异。此外，通过分析纯文本理由中的trope模式，研究发现即使在立场相异的情况下，模型和提示之间也会反复生成相似的论证。

**结论及对未来研究的意义**
研究强调了分析LLMs生成的文本中隐含的价值观和意见的重要性，这有助于改进用户体验和减少潜在危害。通过识别和理解模型生成响应中的模式，可以更好地指导LLMs的开发和应用，特别是在处理敏感话题时，以确保公平性和准确性。

**关键图表与数据**
研究提供了模型响应的气泡图、标准偏差图和稳健性图，显示了不同模型在处理封闭式和开放式问题时的一致性水平，以及在PCT命题上的变异性。这些图表揭示了模型响应的波动程度，以及不同模型间在相同命题上的相似性和差异性。
#   What Matters in Detecting AI-Generated Videos like Sora?
1. **论文标题**  
   - 《检测像Sora这样的AI生成视频的关键因素是什么？》

2. **作者信息**  
   - Chirui Chang, Zhengzhe Liu, Xiaoyang Lyu, Xiaojuan Qi
   - 作者分别来自香港大学(The University of Hong Kong)和香港中文大学(The Chinese University of Hong Kong)

3. **论文标签**  
   - AI视频生成、深度学习、视频真实性检测、3D卷积网络、扩散模型

4. **研究核心目标与问题**  
   - 研究旨在通过从外观、运动和几何三个基本视角比较真实世界视频与最新AI模型生成的视频，探索合成视频与真实视频之间的差距。这有助于揭示AI生成视频的局限性以及提升检测AI生成视频的能力。

5. **采用方法与技术**  
   - 使用3D卷积神经网络训练了三个分类器，分别针对外观（基于视觉基础模型特征）、运动（基于光流）和几何（基于单目深度）。研究还利用Grad-CAM技术来定位AI生成视频在上述三个维度上的系统性失败。

6. **实验设计与主要发现**  
   - 实验设计包括使用Pexels收集的真实世界视频和Stable Video Diffusion模型生成的合成视频作为数据集。分类器在检测AI生成视频方面表现优异，即使是在跨模型场景下，如检测未见过的Sora生成的视频时，准确率也能达到70%。

7. **结论及对未来研究的意义**  
   - 结论指出AI生成的视频在外观、运动和几何上仍存在明显缺陷，无法欺骗简单的3D CNN检测器。研究提出的Ensemble-of-Experts模型通过整合外观、光流和深度信息，提高了检测AI生成视频的鲁棒性和泛化能力。这表明检测模型能够跨越不同的视频生成模型进行有效识别，为未来AI生成视频的检测技术提供了新的方向。

8. **关键图表与数据**  
   - 关键图表包括使用Grad-CAM技术展示的分类器决策依据的可视化结果，以及模型在不同生成模型上检测AI生成视频的准确性数据，如Table 2和Table 3所示，其中“Ours”表示模型在检测Sora生成的视频时超过80%的准确率，即使在训练过程中没有接触过Sora视频。
#   FoleyCrafter: Bring Silent Videos to Life with Lifelike and Synchronized Sounds
1. **论文标题**  
   - FoleyCrafter: 为无声视频添加生动同步音效
   
2. **作者信息**  
   - Yiming Zhang, Yicheng Gu, Yanhong Zeng, Zhening Xing, Yuancheng Wang, Zhizheng Wu, Kai Chen  
   - 机构: 上海人工智能实验室 & 香港中文大学(深圳)

3. **论文标签**  
   - Neural Foley, 自动音效生成, 音频-视频同步, 深度学习

4. **研究核心目标与问题**  
   - 研究旨在通过自动产生高质量、与视频内容语义相关且时间同步的音效，提升无声视频的沉浸式体验。现有方法在同时保证音质和精确对齐方面存在局限性。

5. **采用方法与技术**  
   - 提出了FoleyCrafter框架，利用预训练文本到音频模型确保高质量音频生成。框架包括两个关键组件：语义适配器和时间控制器。前者使用并行交叉注意力层来基于视频特征调节音频生成；后者结合起始检测器和基于时间戳的适配器实现精准音视频同步。

6. **实验设计与主要发现**  
   - 在VGGSound和AVSync15等标准基准上进行了广泛定量和定性实验，验证了FoleyCrafter的有效性。实验结果显示，在语义对齐和音频质量（MKL, CLIP, FID）以及时间同步（起始检测精度和平均精度）方面，FoleyCrafter显著优于现有方法。

7. **结论及对未来研究的意义**  
   - 研究提出了FoleyCrafter，一种用于向无声视频添加高质量、同步音效的神经网络框架，它不仅提升了音效的语义相关性和时间同步性，还提供了通过文本提示可控的多样化音频生成能力，对视频制作和游戏行业有重大意义。

8. **关键图表与数据**  
   - 表1展示了FoleyCrafter在VGGSound和AVSync15数据集上的性能，包括Mean KL Divergence、CLIP相似度和Frechet距离指标，显示其在语义对齐和音频质量方面领先于其他模型。表2比较了不同方法在时间同步方面的表现，FoleyCrafter在起始检测准确率和平均精度上取得最佳成绩。
#   μ-Bench: A Vision-Language Benchmark for Microscopy Understanding
1. **论文标题**  
   - µ-BENCH: VISION-LANGUAGE BENCHMARK FOR MICROSCOPY UNDERSTANDING

2. **作者信息**  
   - Alejandro Lozano, Department of Biomedical Data Science, Stanford University
   - Jeffrey Nirschl, Department of Pathology, Stanford University
   - James Burgess, ICME, Stanford University
   - Sanket Rajan Gupte, Department of Computer Science, Stanford University
   - Yuhui Zhang, Department of Computer Science, Stanford University
   - Alyssa Unell, Department of Computer Science, Stanford University
   - Serena Yeung-Levy, Department of Biomedical Data Science, Stanford University

3. **论文标签**  
   - 微生物图像理解、视觉语言模型、基准测试、生物医学图像分析、细胞生物学、病理学

4. **研究核心目标与问题**  
   - 研究旨在通过创建一个名为µ-Bench的专家策划基准测试集，评估视觉语言模型(VLMs)在生物显微镜图像理解上的感知和认知能力。当前缺乏标准化、多样性和大规模的视觉语言基准，这限制了VLMs在生物图像分析中的有效应用。

5. **采用方法与技术**  
   - 本研究涵盖了22项生物医学任务，跨越多个学科、显微镜模式、尺度和生物状态。使用了来自25个独特数据集的17,235张显微镜图像，涵盖光、荧光和电子显微镜，以及12个子域的96种不同的细胞和组织类型。每张图像都由专家进行了密集注释，生成了5个关于显微镜模式、子模式、领域、子域和染色技术的粗粒度问题和描述。

6. **实验设计与主要发现**  
   - 实验设计包含了13个分类任务和5个分割与对象检测任务，涉及不同难度级别的数据拆分。研究发现，即使在区分显微镜模式等基本任务上，现有模型也面临挑战；专门针对生物医学数据调整的模型往往比通用模型表现差；特定显微镜领域的细调可能会导致性能提升。此外，对比了监督线性模型在DINOv2特征上的性能基线。

7. **结论及对未来研究的意义**  
   - 结论表明，现有的VLMs在所有类别上都存在不足，尤其是在处理复杂生物图像时。这为未来的研究指明了方向，即需要开发更高级的模型来提高生物图像的理解能力，特别是针对特定显微镜领域。

8. **关键图表与数据**  
   - 论文提供了包含86,175个粗粒度问题的数据集，以及根据任务划分的精细结果。例如，GPT-4o在某些任务中表现最佳，但在其他特定任务上，如分子共定位，ALIGN模型胜出，而在线粒体形态分类上，BiomedCLIP表现最优。这些数据点和分析结果对于理解模型在不同生物医学任务上的性能至关重要。