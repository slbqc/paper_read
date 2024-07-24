
#   Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies
**论文标题**
   - Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies

**作者信息**
   - Chaofan Tao, Qian Liu, Longxu Dou, Niklas Muennighoff, Zhongwei Wan, Ping Luo, Min Lin, Ngai Wong
   - 机构：香港大学(The University of Hong Kong), 海洋AI实验室(Sea AI Lab), Contextual AI, 俄亥俄州立大学(The Ohio State University)

**论文标签**
   - 大型语言模型(LLMs)，词汇规模，模型参数，训练数据量，计算预算，最优词汇规模

**研究核心目标与问题**
   - 该研究聚焦于大型语言模型(LLMs)的词汇规模对模型性能的影响，传统研究多关注模型参数和训练数据量，而忽视了词汇规模的作用。

**采用方法与技术**
   - 训练了从33M到3B参数的模型，在最多500B字符的数据集上，使用不同词汇配置进行训练。
   - 提出了三种互补的方法来预测计算最优的词汇规模：等FLOPs分析(IsoFLOPs analysis)、导数估计(derivative estimation)和损失函数的参数拟合(parametric fit of the loss function)。

**实验设计与主要发现**
   - 实验设计覆盖了不同FLOPs预算下的3B参数模型训练，验证了预测的最优词汇规模可以持续提升下游任务性能。
   - 结果显示，Llama2-70B模型的最优词汇规模应至少为216K，远大于其实际使用的32K词汇规模。

**结论及对未来研究的意义**
   - 研究强调了在高效扩展模型时，同时考虑模型参数和词汇规模的必要性。
   - 增加词汇规模至预测的最优值，可以显著提高模型性能，如将词汇规模从32K增加到43K，ARC-Challenge上的性能从29.1提升到了32.0，而FLOPs保持不变。

**关键图表与数据**
   - 图1展示了非词汇参数Nnv与其最优词汇参数Noptv之间的幂律关系，表明词汇参数的扩展速率应慢于非词汇参数(γ< 1)。
#   Scaling Retrieval-Based Language Models with a Trillion-Token Datastore
1. **论文标题**  
   - 通过万亿级语料库扩展检索式语言模型的规模

2. **作者信息**  
   - Rulin Shao, Jacqueline He, Akari Asai, Weijia Shi, Tim Dettmers, Sewon Min, Luke Zettlemoyer, Pang Wei Koh
   - 华盛顿大学，艾伦人工智能研究所

3. **论文标签**  
   - 语言模型，大规模数据集，检索增强，自然语言处理，知识密集型任务

4. **研究核心目标与问题**  
   - 本研究探索了在推理阶段增加数据量对语言模型（LM）性能的影响，特别是在知识密集型任务上的表现。

5. **采用方法与技术**  
   - 构建了一个名为MASSIVEDS的1.4万亿令牌数据仓库，这是迄今为止为检索式语言模型提供的最大、最多样化的开源数据仓库。
   - 设计了一种高效的管道，以计算可访问的方式研究数据仓库的扩展性。
   - 使用不同的数据仓库大小、模型大小和预训练数据量绘制了计算最优的扩展曲线。

6. **实验设计与主要发现**  
   - 实验发现，增大用于检索式LM的数据仓库大小可以单调地提升语言建模和多个下游任务的表现，没有明显的饱和现象。
   - 结果表明，较小的模型加上大型数据仓库，在知识密集型任务上能超越仅使用较大LM模型的表现。
   - 在相同的训练计算预算下，使用更大的数据仓库能显著提高模型性能。

7. **结论及对未来研究的意义**  
   - 数据仓库的大小应被视为语言模型效率和性能权衡的一个组成部分。
   - 开源数据仓库和代码将促进未来的研究。

8. **关键图表与数据**  
   - 论文中的图1展示了不同配置下的模型大小、数据仓库扩展以及下游任务表现的关系，突出了数据仓库大小对模型性能的重要影响。
#   Shape of Motion: 4D Reconstruction from a Single Video
# faild to  read !!!!
#   Streetscapes: Large-scale Consistent Street View Generation Using Autoregressive Video Diffusion
**论文标题**
   - Streetscapes: Large-scale Consistent Street View Generation Using Autoregressive Video Diffusion

**作者信息**
   - Boyang Deng, Stanford University USA
   - Richard Tucker, Google Research USA
   - Zhengqi Li, Google Research USA
   - Leonidas Guibas, Stanford University & Google Research USA
   - Noah Snavely*, Google Research USA
   - Gordon Wetzstein*, Stanford University USA

**论文标签**
   - 计算机视觉, 神经网络, 图像合成, 视频合成, 生成模型, 扩散模型, 场景生成, 神经渲染

**研究核心目标与问题**
   - 本研究旨在解决大规模城市场景下一致且高质量的街景视图生成问题。具体目标是生成长序列的街景图像，这些图像能够沿着城市尺度的虚拟路径保持布局控制和风格一致性。

**采用方法与技术**
   - 使用自回归视频扩散模型结合文本输入和底层地图布局来生成街景。该模型基于预训练的文本到图像的扩散模型，通过运动模块和ControlNet实现两帧生成，同时利用G-buffer条件来控制相机姿态和场景布局。

**实验设计与主要发现**
   - 实验设计包括使用谷歌街景数据集进行训练，以及对比实验评估生成视图的质量和一致性。研究发现，所提出的系统能够生成高质量、长范围一致的街景视图，显著优于现有方法如InfiniCity和InfNat0，在所有自回归步骤上保持更好的质量。

**结论及对未来研究的意义**
   - 结论指出，Streetscapes系统能够生成高保真度、一致性的街景视图，受控于场景布局、相机姿态和可选的文字输入风格。这项工作标志着视觉生成模型向前迈出一步，从物体级生成扩展到了无限大规模场景的生成能力。

**关键图表与数据**
   - 图1展示了Streetscapes系统的概念图，图2详细说明了布局条件下的场景生成过程，而表1和表2提供了与现有方法比较的关键性能指标，如FID和KID值，以及近程准确性测量LPIPS值。
#   Understanding Reference Policies in Direct Preference Optimization
**论文标题**
   - Understanding Reference Policies in Direct Preference Optimization

**作者信息**
   - Yixin Liu1, Pengfei Liu2, Arman Cohan1,3
   - 1Yale University, 2Shanghai Jiao Tong University, 3Allen Institute for AI
   - yixin.liu@yale.edu, pengfei@sjtu.edu.cn, arman.cohan@yale.edu

**论文标签**
   - 大型语言模型、直接偏好优化(DPO)、强化学习、参考策略、指令微调

**研究核心目标与问题**
   - 本研究旨在深入探索直接偏好优化(DPO)训练方法中一个较少被关注的方面——参考策略或政策的作用。DPO是大型语言模型(LLM)指令微调的常用训练方法，但其效果可能受限于所选参考模型的质量。因此，研究集中探讨了三个相关问题：1) DPO中KL散度约束的最佳强度；2) 指令微调中是否需要参考策略；3) 强化参考策略是否能提升DPO表现。

**采用方法与技术**
   - 研究采用了理论分析和实证比较的方法，通过调整DPO中的KL散度约束强度、比较DPO与其他学习目标以及测试不同强度的参考策略，来探究上述问题。

**实验设计与主要发现**
   - 实验设计围绕指令微调任务进行，使用开源预训练LLM Tulu 2和Mistral，以及AlpacaEval基准数据集。主要发现包括：1) 较小的KL约束强度通常能改善性能，直到过小导致性能下降；2) DPO在指令学习中优于其他相关目标；3) 强化参考策略可以提高性能，但仅当它与待微调模型兼容时。

**结论及对未来研究的意义**
   - 结论指出，DPO中参考策略的作用复杂且具有决定性，最佳实践包括：使用适度的KL约束以及确保参考策略与待微调模型兼容。同时，研究强调了对参考策略必要性的开放性问题，呼吁更多理论分析。

**关键图表与数据**
   - 论文提及的关键数据包括不同KL约束强度下的模型性能对比、奖励函数参数化下的模型排名准确性，以及使用强化参考策略时的性能变化。这些数据点揭示了DPO训练动态和参考策略的重要作用。
#   Scaling Granite Code Models to 128K Context
**论文标题**
- IBM Long Context Granite Code Models: Scaling Granite Code Models to 128K Context

**作者信息**
- Matt Stallone, Vaibhav Saxena, Leonid Karlinsky, Bridget McGinn, Tim Bula, Mayank Mishra, Adriana Meza Soria, Gaoyuan Zhang, Aditya Prasad, Yikang Shen, Saptha Surendran, Shanmukha Guttula, Hima Patel, Parameswaran Selvam, Xuan-Hong Dang, Yan Koyfman, Atin Sood, Rogerio Feris, Nirmit Desai, David D. Cox, Ruchir Puri, Rameswar Panda
- IBM Research

**论文标签**
- 长上下文编码模型
- 大型语言模型
- 软件开发
- 代码生成
- 上下文扩展

**研究核心目标与问题**
- 本研究旨在解决当前开源代码语言模型在长上下文处理能力上的局限性，通过扩展模型的有效上下文窗口至128K令牌，提升其在实际软件开发中的实用性。

**采用方法与技术**
- 研究团队使用轻量级持续预训练方法，逐步增加RoPE基频，结合仓库级别文件打包和长度上采样的长上下文数据，扩展了Grande Code模型的上下文长度。
- 进一步地，通过微调指令调整模型，利用短和长上下文指令响应对的混合数据集进行训练。

**实验设计与主要发现**
- 实验设计包括在多种基准测试上评估模型性能，如HumanEvalPack、Long Code Completion、RepoBench-P、RepoQA和Key Retrieval。
- 结果显示，长上下文模型在长序列任务上的表现显著提高，同时在常规代码完成基准测试中没有明显性能下降。

**结论及对未来研究的意义**
- 研究表明，长上下文Granite代码模型能够有效利用长上下文信息，改善代码生成质量，而不会牺牲短上下文任务的性能。
- 该成果有望推动长上下文处理在软件开发领域的应用，并为后续研究提供了新的方向。

**关键图表与数据**
- 表1和表2展示了不同上下文长度下长上下文模型与原模型在LCC和RepoBench-P基准上的性能对比。
- 图1直观地比较了长上下文模型与短上下文模型在相似度阈值为0.5时的检索精度差异。
#   Benchmarking Trustworthiness of Multimodal Large Language Models: A Comprehensive Study
**论文标题**
   - Benchmarking Trustworthiness of Multimodal Large Language Models: A Comprehensive Study

**作者信息**
   - 张一驰1,4∗†, 黄垚2∗, 孙逸彤2, 刘畅3, 赵哲4, 方政威1, 王一帆1, 陈焕然1, 杨潇1, 魏兴星2, 苏航1, 董银鹏1,4†, 朱军1,4
   - 作者分别来自清华大学、北京航空航天大学、上海交通大学等机构。

**论文标签**
   - 多模态大语言模型、可信度评估、基准测试、信任度、安全、鲁棒性、公平性、隐私

**研究核心目标与问题**
   - 本研究旨在解决多模态大型语言模型（MLLM）在多种任务上的信任度挑战，通过建立首个全面统一的评估基准MultiTrust，评估模型在真实、安全、鲁棒性、公平性和隐私保护五个方面的性能，以促进未来改进的方向。

**采用方法与技术**
   - 研究使用了严格的评估策略，涵盖32种不同任务的自编数据集，设计用于评估多模态风险和跨模态影响，涉及文本、图像等多种输入形式。

**实验设计与主要发现**
   - 实验涉及21个现代MLLM模型，揭示了之前未被探索的信任度问题和风险，如模型在视觉混淆图像识别中的困难、多模态越狱和对抗攻击的脆弱性，以及在文本中泄露隐私和展示意识形态偏见的倾向。
   - 结果显示，当前MLLM在需要更高细粒度要求的任务上表现下降，模型间差异更加明显；在常识推理任务上优于基于能力的问题；对不同提示的敏感性各异，提示设计有助于整体预测性能提升；额外的正面图像输入可以改善仅文本任务的性能；非关键描述部分的事实错误会影响响应准确性；面对复杂视觉现象时容易出错，尤其是挑战认知能力的情况。

**结论及对未来研究的意义**
   - 研究强调了多模态环境下模型可靠性的复杂性，为改进MLLM的可信度提供了重要见解，指出了模型设计和训练过程中的关键问题，为未来研究指明了方向。

**关键图表与数据**
   - 提供了不同模型在Truthfulness、Safety、Robustness、Fairness和Privacy五个方面评分和排名的关键数据，展示了模型在不同子任务上的表现，如Robustness下的OOD（Out-of-Distribution）和Adversarial Attack，以及Privacy下的Privacy Leakage等具体指标。
#   Attention Overflow: Language Model Input Blur during Long-Context Missing Items Recommendation
**论文标题**
   - Attention Overflow: Language Model Input Blur during Long-Context Missing Items Recommendation

**作者信息**
   - Damien Sileo, Univ. Lille, Inria, CNRS, Centrale Lille, UMR 9189- CRIStAL, F-59000 Lille, France

**论文标签**
   - Large Language Models (LLMs)
   - Missing Item Prediction
   - Attention Overflow
   - Recommendation Systems
   - Context Length Stress Testing

**研究核心目标与问题**
   - 研究关注于大型语言模型（LLMs）在处理长序列输入时推荐缺失项的能力。当输入项过多时，LLMs倾向于重复输入列表中的已有元素，而非推荐新元素，这被称为“注意力溢出”现象。该研究评估了这一现象在合成问题和电影推荐场景下的表现。

**采用方法与技术**
   - 使用多种大型语言模型进行零样本测试，包括Llama、Gemini、GPT-4o和Claude，以评估它们在不同大小的输入集上预测缺失项的能力。
   - 实施微调策略，使用Llama-3 Instruct 8B模型进行特定任务的训练，以探索是否能改善预测性能。

**实验设计与主要发现**
   - 在数值范围和电影推荐的合成问题上进行了实验，结果显示，随着输入项数量增加至约100个，所有模型的准确性下降，重复率上升。
   - 微调可以提高特定域内的缺失项预测，但效果无法推广到更大规模的输入集或不同领域。

**结论及对未来研究的意义**
   - 结论表明，当前的注意力机制可能不足以处理大量相似输入的比较，提示未来研究需要探索更深层次的模型架构或新的注意力机制，以克服这一限制。
   - 对于推荐系统领域，该研究强调了在处理用户历史记录时，防止重复推荐的重要性，以及当前LLMs在处理此类任务时的局限性。

**关键图表与数据**
   - 图1展示了随着输入项目数量的增加，不同模型在数字和电影推荐任务上的准确性与重复率的变化趋势。
   - 图2通过对比微调前后的Llama-3模型在不同领域数据上的表现，说明了微调在特定域内可提升性能，但在泛化能力方面存在不足。
   - 图3展示了Llama-3-8B-Instruct在判断列表中是否存在某一元素时的准确率随输入项增加的变化情况，维持在75%左右的水平。
#   CodeV: Empowering LLMs for Verilog Generation through Multi-Level Summarization
**论文标题**  
   - CodeV: Empowering LLMs for Verilog Generation through Multi-Level Summarization

**作者信息**  
   - Yang Zhao, Di Huang, Chongxiao Li, Pengwei Jin, Ziyuan Nan, Tianyun Ma, Lei Qi, Yansong Pan, Zhenxing Zhang, Rui Zhang, Xishan Zhang, Zidong Du, Qi Guo, Xing Hu, Yunji Chen
   - 中国科学院计算技术研究所处理器重点实验室、中国科学院大学、中国科学技术大学、寒武纪科技

**论文标签**  
   - 大型语言模型、Verilog生成、硬件描述语言、代码自动生成、处理器设计自动化

**研究核心目标与问题**  
   - 针对现代处理器设计中复杂度增加和成本高昂的问题，本文提出了一种利用大型语言模型（LLMs）自动进行Verilog代码生成的方法。传统LLMs在通用编程语言如Python上表现出色，但在硬件描述语言HDL（如Verilog）上的表现受限于高质量指令调优数据的稀缺性。

**采用方法与技术**  
   - 引入了CodeV，一系列开源的、针对指令调优的Verilog生成LLMs。研究者观察到实际收集的Verilog代码质量高于LLMs生成的代码，且GPT-3.5等LLMs更擅长总结而非生成Verilog代码。基于此，研究通过多级总结的方式，让LLM从Verilog代码生成自然语言描述，而非先生成描述再得到代码。

**实验设计与主要发现**  
   - 实验结果显示，CodeV在VerilogEval和RTLLM两个评估指标上分别超越了先前的开源最佳模型14.4%和11.3%，并且在VerilogEval上相对商业顶级模型GPT-4提升了22.1%。

**结论及对未来研究的意义**  
   - CodeV展示了在Verilog代码生成领域的显著改进，为处理器设计自动化提供了新的解决方案。未来的研究可以进一步探索LLMs在硬件设计自动化中的应用潜力，以及如何更有效地训练和优化这些模型以适应复杂的硬件描述任务。

**关键图表与数据**  
   - 图3展示了多级总结的实际示例，包括提供给GPT-3.5的提示、代码、低级描述、高级总结的示例，以及使用和不使用多级总结时GPT-3.5的响应对比。
#   CLAY: A Controllable Large-scale Generative Model for Creating High-quality 3D Assets
1. **论文标题**  
   - CLAY: A Controllable Large-scale Generative Model for Creating High-quality 3D Assets

2. **作者信息**  
   - LONGWEN ZHANG\*, ZIYU WANG\*, QIXUAN ZHANG†, QIWEI QIU, ANQI PANG, HAORAN JIANG, WEI YANG, LAN XU‡, JINGYI YU‡
   - 上海科技大学, 德摩斯科技有限公司, 华中科技大学

3. **论文标签**  
   - 3D生成模型, 大规模生成, 高质量3D资产, 数字创意, 控制性

4. **研究核心目标与问题**  
   - 研究旨在通过引入CLAY——一种可控的大规模生成模型, 解决数字创意领域中从想象创造复杂3D世界时受到现有工具限制的问题, 这些工具往往需要大量的专业知识和努力。

5. **采用方法与技术**  
   - CLAY被设计为一个能够轻松地将人类想象力转化为高质量3D几何和材质的生成器。它采用了深度学习和机器学习技术, 包括但不限于Transformer架构和Diffusion模型, 来生成复杂的3D形状和纹理。

6. **实验设计与主要发现**  
   - 实验比较了CLAY与其他领先的文本到3D的方法, 如Shap-E、DreamFusion、Magic3D、MVDream和RichDreamer。实验结果显示CLAY能够在大约45秒内产生高质量的3D资产, 其中几何体和纹理分别在5秒和40秒内完成。生成的几何体具有平滑的表面, 同时保持细节的完整性, 更好地匹配文本提示。

7. **结论及对未来研究的意义**  
   - CLAY提供了一种高效且可控的方式, 可以生成具有精细细节和平滑表面的高质量3D资产, 大大缩短了从概念到成品的时间。这一成果对3D内容创作领域具有重要意义, 特别是在游戏开发、虚拟现实和增强现实应用中。

8. **关键图表与数据**  
   - 图1展示了CLAY如何在广阔的数字领域中激发3D创造力, 释放无限的想象力。图11评估了几何多样性, 展示了从数据集中检索到的前3个最近邻样本, 强调了CLAY生成的高质几何体与数据集中的区别。表5提供了与最先进的方法进行定量比较的数据, 显示CLAY在Text-to-3D任务上的性能优势。
#   BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval
1. **论文标题**  
   - BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval

2. **作者信息**  
   - 香港大学的Hongjin Su, Tao Yu; 普林斯顿大学的Howard Yen, Mengzhou Xia, Weijia Shi, Niklas Muennighoff, Hanyu Wang, Haisu Liu, Quan Shi, Zachary S. Siegel, Michael Tang, Ruoxi Sun, Jinsung Yoon, Danqi Chen; 华盛顿大学的Danqi Chen; Google Cloud AI Research的Sercan Ö. Arık.

3. **论文标签**  
   - 文本检索, 基准测试, 深度推理, 大型语言模型, 链式思考

4. **研究核心目标与问题**  
   - 研究旨在开发一个全新的文本检索基准测试——BRIGHT，该基准要求深度的逻辑推理能力以识别相关文档，解决了现有检索基准测试中仅依赖关键字或语义匹配的问题。通过收集来自不同领域的1,398个真实世界查询，BRIGHT旨在推动检索系统对复杂查询的处理能力。

5. **采用方法与技术**  
   - 为了构建BRIGHT，作者从多个领域收集了自然发生或精心策划的人类数据，这些数据需要深度理解才能正确检索。此外，通过使用大型语言模型生成链式思考推理步骤来增强查询，以改进检索性能。

6. **实验设计与主要发现**  
   - 实验中，作者评估了最先进的检索模型在BRIGHT上的表现，发现即使是MTEB排行榜上领先的模型，在BRIGHT上的nDCG@10得分仅为18.0，远低于其在其他基准上的59.0得分。引入链式思考推理后，模型性能提高了12.2点。实验还验证了即使训练数据中包含基准文档，BRIGHT也能够抵抗预训练数据泄露的影响。

7. **结论及对未来研究的意义**  
   - BRIGHT为检索领域提供了新的挑战，强调了当前模型在处理需要深度推理的查询时的局限性。它为未来的研究开辟了道路，鼓励开发能更好理解和推理的检索模型。

8. **关键图表与数据**  
   - 表3展示了在BRIGHT上的重新排序性能，包括使用LLM进行重新排序的结果，以及与原始查询相比，使用LLM推理步骤作为查询显著提高的性能。这表明利用LLM的链式思考能力可以显著提升检索效果。
#   Retrieval-Enhanced Machine Learning: Synthesis and Opportunities
1. **论文标题**  
   - Retrieval-Enhanced Machine Learning: Synthesis and Opportunities

2. **作者信息**  
   - TO EUN KIM, Carnegie Mellon University, United States  
   - ALIREZA SALEMI, University of Massachusetts Amherst, United States  
   - ANDREW DROZDOV, University of Massachusetts Amherst, United States  
   - FERNANDO DIAZ, Carnegie Mellon University, United States  
   - HAMED ZAMANI, University of Massachusetts Amherst, United States

3. **论文标签**  
   - 自然语言处理(NLP)  
   - 机器学习(ML)  
   - 信息检索(IR)  
   - 大型语言模型(LLMs)

4. **研究核心目标与问题**  
   - 本研究旨在解决自然语言处理领域面临的挑战，如知识接地、可解释性和可扩展性，通过增强机器学习模型的检索组件。研究强调了检索增强范式在计算机视觉、时间序列预测和计算生物学等更广泛领域的潜力。

5. **采用方法与技术**  
   - 论文提出了一种正式框架，即检索增强机器学习(REML)，通过综合不同领域的文献，使用一致的符号系统来填补现有文献中的空白。此外，研究还探讨了REML框架的各个组成部分，以缩小基础信息检索研究与当代REML研究之间的差距。

6. **实验设计与主要发现**  
   - 研究分析了REML系统的不同组成部分，包括文档的呈现（如翻译、去上下文化、总结）、结果项的组合、结果列表的截断以及统一的呈现方程。此外，讨论了耦合存储在REML系统中的作用，包括其冷启动问题、适应性和在不同任务间的迁移能力。

7. **结论及对未来研究的意义**  
   - 该工作为跨学科的研究者提供了一个全面、正式的REML框架，旨在促进检索增强模型在多个学科中的未来发展。通过解决REML系统的关键问题，如数据加载效率和外部数据动态需求，研究有助于推动REML在实际应用中的进步。

8. **关键图表与数据**  
   - 提供了关于呈现相关研究实例的表格，包括ALCE、Teach LLMs to Personalize、QADecontext等方法，这些实例展示了总结、提取片段、去上下文化等技术的应用。此外，还提到了消费阶段的研究，虽然未详细列出具体数据，但突出了在REML系统中处理和利用检索到的文档的有效性。
#   A Comparative Study on Automatic Coding of Medical Letters with Explainability
**论文标题**
自动医疗信函编码的比较研究与可解释性

**作者信息**
Jamie Glen, Lifeng Han, Paul Rayson, Goran Nenadic
兰卡斯特大学, 曼彻斯特大学, 英国

**论文标签**
自然语言处理(NLP), 机器学习(ML), 自动编码, 医疗信函, 可解释性, 临床编码, SNOMED CT, ICD代码

**研究核心目标与问题**
本研究旨在探索自然语言处理(NLP)和机器学习(ML)技术在自动化医疗信函编码中的应用,特别关注在本地计算机设置下的轻量级实现以及模型的可视化可解释性。当前临床环境中,编码过程仍依赖人工,涉及为患者文件中的每个病症、手术和药物分配特定代码(例如使用SNOMED CT代码为心脏病编码)。研究的目标是开发一个原型系统,以辅助编码人员加快编码过程,并探讨此类系统在实际环境中的集成可能性。

**采用方法与技术**
研究利用了公开的MIMIC-III数据库和HAN/HLAN网络模型进行ICD代码预测,同时实验了ICD与SNOMED CT知识库之间的映射。研究中使用的模型提供了对97.98%编码的有用信息。

**实验设计与主要发现**
研究设计包括预处理医疗文本、使用HAN模型进行ICD代码预测、将ICD代码转换为SNOMED CT代码,以及提供编码决策的可视化。实验结果显示,模型能够成功地将ICD代码映射到SNOMED CT代码,并在大多数情况下给出有用的响应。

**结论及对未来研究的意义**
研究成功实现了自动医疗文本编码,并提供了编码决策的解释,这在医疗编码实践中具有重要价值,特别是在医院环境中。未来工作可能包括创建更符合实际应用的数据集,以提高模型的泛化能力,以及探索深度学习解决方案在医疗编码领域的应用。

**关键图表与数据**
研究展示了模型在MIMIC-III-50和MIMIC-III-Full数据集上的性能,包括微平均F1分数、宏平均F1分数和精度指标。此外,还提供了编码映射的统计数据,显示了1对1映射、1对多映射、无映射和无描述的情况百分比。
#   Benchmark Agreement Testing Done Right: A Guide for LLM Benchmark Evaluation
**论文标题**
   - Benchmark Agreement Testing Done Right: A Guide for LLM Benchmark Evaluation

**作者信息**
   - Yotam Perlitz, Ariel Gera, Ofir Arviv, Asaf Yehudai, Elron Bandel, Eyal Shnarch, Michal Shmueli-Scheuer, Leshem Choshen
   - IBM Research AI, MIT CSAIL, MIT-IBM Watson AI Lab

**论文标签**
   - 大型语言模型评估, 基准测试, 协议测试, 标准化流程

**研究核心目标与问题**
   - 该研究旨在解决大型语言模型（LLMs）基准测试中的协议测试（Benchmark Agreement Testing, BAT）标准化问题，以确保基准的有效性和可靠性。

**采用方法与技术**
   - 分析了超过40个知名基准测试，探讨了不同方法论选择如何显著影响BAT结果。
   - 提出了最佳实践指南，包括选择参考基准、模型选取、相关性度量和阈值设定，以及使用数据驱动的方法来解释协议分数。

**实验设计与主要发现**
   - 实验中考虑了参考基准的选择、模型数量和特性、相关性度量及其解释等多个因素的影响。
   - 发现了不同的方法论选择可以极大地改变BAT的结论，强调了标准化方法的重要性。

**结论及对未来研究的意义**
   - 结论指出标准化的BAT对于保证基准评价的稳健性和有效性至关重要。
   - 对未来的研究有重要指导意义，促进基准创建者和使用者之间的信任，帮助选择合适的基准进行模型评估。

**关键图表与数据**
   - 图表展示了不同模型集合下基准之间的协议分数变化，以及不同相关性度量之间的线性关系。
   - 数据分析表明，遵循提出的最佳实践可以显著减少BAT结果的方差，提高其稳定性和有效性。
#   PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks
**论文标题**
- PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks

**作者信息**
- Alessandro Berti, Humam Kourani, Wil M. P. van der Aalst
- 机构: Process and Data Science Chair, RWTH Aachen University, Aachen, Germany & Fraunhofer FIT, Sankt Augustin, Germany

**论文标签**
- Process Mining, Large Language Models, Evaluation Strategies, LLM Benchmarking

**研究核心目标与问题**
- 本研究旨在评估大型语言模型（LLMs）在流程挖掘（Process Mining, PM）任务中的性能，特别是针对领域知识（流程挖掘特有和流程特定知识）和不同实施策略的全面基准测试。

**采用方法与技术**
- 提出了PM-LLM-Benchmark，这是第一个专注于流程挖掘领域的全面基准测试，涵盖直接提供洞察和代码生成两种实施策略。研究还关注了创建此类基准测试时面临的挑战，如数据公开可用性和LLMs评价偏见的问题。

**实验设计与主要发现**
- 实验设计基于一系列“静态”提示，要求模型展示流程挖掘特有和流程特定的领域知识。研究发现大多数考虑的LLMs能在一定程度上执行流程挖掘任务，但小型模型在边缘设备上的表现仍不理想。

**结论及对未来研究的意义**
- 尽管提出的基准测试有助于识别适合流程挖掘任务的LLMs，但仍需进一步研究以克服评价偏见，更彻底地排名“竞争性”的LLMs。这为未来研究提供了方向，尤其是在评估策略和模型能力方面。

**关键图表与数据**
- 提供了不同LLMs在多种流程挖掘任务上的平均得分（1.0至10.0之间），展示了商业模型和大型开源模型在这些任务上的出色表现，而小型和微型模型则在复杂任务上挣扎。此外，报告了每个模型类别和问题类别的具体得分，以及单个提示的平均得分，为理解模型在不同任务上的表现提供了深入见解。