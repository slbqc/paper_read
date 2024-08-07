import asyncio
from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
)
from metagpt.team import Team

async def startup(idea: str):
    company = Team()
    company.hire(
        [
            ProductManager(),
            Architect(),
            ProjectManager(),
            Engineer(),
        ]
    )
    company.invest(investment=3.0)
    company.run_project(idea=idea)

    await company.run(n_round=5)

async def initialize_game_resources(idea="write a cli blackjack game"):
    """
    异步初始化游戏资源函数。
    
    此函数旨在游戏启动前完成必要的资源初始化，如加载配置、准备数据库连接等。
    参数:
        idea (str): 初始化资源时的日志提示信息。默认为"write a cli blackjack game"。
    
    返回:
        无
    """
    try:
        await startup(idea=idea)  # 假设startup是一个异步函数，用于实际的资源初始化
        print("游戏资源初始化成功。")
    except Exception as e:
        # 在实际应用中，应该使用更具体的异常类，而不是捕获所有异常
        print(f"游戏资源初始化失败：{e}")
        # 根据实际情况考虑是否需要重新抛出异常或者如何恢复状态

# 假设以下为你的主程序入口
async def main():
    """
    主程序入口函数。
    
    负责调用初始化函数并开始游戏循环。
    """
    # 进行游戏资源初始化
    await initialize_game_resources(idea="write a cli blackjack game")

    # 此处添加游戏循环等其他逻辑
    pass

if __name__ == "__main__":
    # 注意：为了运行异步代码，你需要一个事件循环。
    # 在生产环境中，你可能需要更复杂的错误处理和日志记录。
    import asyncio

    asyncio.run(main())