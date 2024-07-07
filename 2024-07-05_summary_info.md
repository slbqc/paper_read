
# paper: Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion
**论文标题**
Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion

**作者信息**
- Boyuan Chen, MIT CSAIL
- Diego Martí Monso, Technical University of Munich
- Yilun Du, MIT CSAIL
- Max Simchowitz, MIT CSAIL
- Russ Tedrake, MIT CSAIL
- Vincent Sitzmann, MIT CSAIL

**论文标签**
- 序列建模
- 扩散模型
- 自回归模型
- 视频预测
- 决策制定

**研究核心目标与问题**
本文提出了一种新的训练范式——Diffusion Forcing，它训练扩散模型以独立的每令牌噪声级别去噪一组令牌。该方法结合了next-token预测模型和全序列扩散模型的优点，即能够生成可变长度的序列并指导采样走向期望的轨迹。其目标是解决序列生成任务中的长序列生成和决策规划问题。

**采用方法与技术**
Diffusion Forcing通过训练因果next-token预测模型来生成一个或多个未来的令牌，而不完全扩散过去的令牌。这种方法允许模型生成连续令牌序列，如视频，其长度超出训练范围，这是基线方法无法达到的。此外，还引入了新的采样和指导方案，这些方案从Diffusion Forcing的可变范围和因果架构中获益，从而在决策和规划任务上显著提高性能。

**实验设计与主要发现**
实验设计围绕视频生成、基于模型的规划、视觉模仿学习和时间序列预测等领域展开，展示了CDF的独特能力，如稳定长时间自动回归视频生成，以及组合训练时观察到的子序列。研究中还介绍了一种名为Monte Carlo Tree Guidance的新能力，它相比非因果全序列扩散模型，在高奖励生成的采样方面有显著改进。

**结论及对未来研究的意义**
Diffusion Forcing作为一种概率序列模型，既具有next-token预测模型的灵活性，又能像全序列扩散模型一样执行长范围指导。通过利用因果性和灵活的噪声调度，CDF能够实现全新的功能，如Monte Carlo Tree Guidance，这在高奖励生成的采样上表现出了显著的改进。理论证明表明，在适当的条件下，优化提出的训练目标最大化了所有在训练时观察到的子序列联合分布的似然率的下界。

**关键图表与数据**
论文的关键图表包括图2，概述了Diffusion Forcing的方法，显示了与next-token预测模型和全序列扩散模型相比，如何将序列的时间轴和扩散的噪声轴交织在一起，统一了两者的优势。实验部分提供了不同领域内的定量和定性结果，验证了CDF在长序列生成稳定性、子序列组合以及高奖励生成方面的独特优势。
# paper: Let the Expert Stick to His Last: Expert-Specialized Fine-Tuning for Sparse Architectural Large Language Models
### **论文标题**
   - 《让专家专精其领域：针对稀疏架构大型语言模型的专家特化微调》

### **作者信息**
   - Zihan Wang, Deli Chen, Damai Dai, Runxin Xu, Zhuoshu Li, Y. Wu
   - 机构：DeepSeek AI, Northwestern University

### **论文标签**
   - 大型语言模型, 参数高效微调(PEFT), 专家混合架构(MoE), 稀疏架构, 专家特化微调(ESFT)

### **研究核心目标与问题**
   - 本研究旨在探讨大型语言模型(Large Language Models, LLMs)的参数高效微调(PEFT)策略，特别是针对具有专家混合架构(Mixture-of-Experts, MoE)的稀疏架构LLMs，解决资源受限环境下定制化任务的适应性问题。

### **采用方法与技术**
   - 提出了专家特化微调(Expert-Specialized Fine-Tuning, ESFT)，一种专门调整与下游任务最相关的专家模块，同时冻结其他专家和组件的方法，显著提高了微调效率和性能。
   - 分析了MoE架构下专家特化的微调效果，发现更细粒度的专家模型能更有效地挑选与下游任务关联度最高的专家组合，优化训练效率和效果。

### **实验设计与主要发现**
   - 实验对比了ESFT与其他微调方法（如FFT和LoRA）在多个任务上的表现，结果显示ESFT不仅提高了调优效率，而且在多数情况下达到了或超过了全参数微调的性能。
   - 在一般任务上，混合对齐数据可以提升FFT和LoRA的表现，但对于ESFT，这种混合并未带来明显优势，突显了ESFT对下游任务的适应性和在一般任务上最小的性能损失。

### **结论及对未来研究的意义**
   - 结论证实，ESFT在训练时间和存储空间方面表现出色，显著优于FFT，且所需的可训练参数远少于FFT，降低了GPU内存使用率。
   - 未来研究应继续探索专家相关性评分和细粒度专家模型结构的重要性，以及如何在不同计算约束下优化ESFT和LoRA的性能。

### **关键图表与数据**
   - 图2和图3展示了专家路由在相同任务中的集中度和跨任务活跃专家的显著变化，证明了MoE模型中专家的专业化。
   - 表3显示ESFT相比FFT在参数量和GPU内存使用方面的优势，表9和表10则提供了不同微调方法在混合数据下的性能对比，突出ESFT在特定任务上的优越表现。
# paper: Planetarium: A Rigorous Benchmark for Translating Text to Structured Planning Languages
1. **论文标题**  
   - Planetarium: 一种严谨的基准测试，用于将文本转换为结构化规划语言

2. **作者信息**  
   - Max Zuo, Francisco Piedrahita Velez, Xiaochen Li, Michael L. Littman, Stephen H. Bach
   - 所属机构：布朗大学计算机科学系

3. **论文标签**  
   - 自然语言处理, 规划问题, 语言模型评估, 结构化规划语言, PDDL

4. **研究核心目标与问题**  
   - 本研究旨在创建一个全面的基准测试Planetarium，以评估语言模型从自然语言描述转换到结构化规划语言（如PDDL）的能力。当前评估方法存在不足，因为它们仅验证生成的PDDL代码是否可解，而忽略了代码与原始任务描述的一致性。

5. **采用方法与技术**  
   - 研究团队开发了一种PDDL等价性算法，通过灵活比较生成的PDDL代码与标准PDDL来严格检验其正确性。此外，他们构建了一个包含132,037个文本到PDDL对的数据集，覆盖13种不同难度的任务。

6. **实验设计与主要发现**  
   - 实验设计涵盖了从显式到抽象再到显式的不同任务描述水平以及问题规模的变化。评估结果表明，尽管GPT-4o生成的87.6% PDDL问题是语法解析的，82.2%是有效的可解决问题，但只有35.1%在语义上是正确的，这凸显了建立更严格基准测试的必要性。

7. **结论及对未来研究的意义**  
   - Planetarium基准测试填补了现有评估体系的空白，能够揭示语言模型在复杂任务中的表现。它强调了需要更细致地评估语言模型在将自然语言转换为结构化规划语言时的准确性和语义一致性。

8. **关键图表与数据**  
   - 图3展示了GPT-4o在不同抽象水平上的零样本性能分解，显示了在不同抽象程度下问题的解析率、可解性和正确性百分比。