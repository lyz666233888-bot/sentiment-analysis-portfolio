# 用户评论情感分析 | Review Sentiment Analysis

将英文 Amazon 商品评论分类为负面或正面，比较 TF-IDF + Logistic Regression 与微调 DistilBERT。项目正在复现阶段，尚未产生新的独立测试集成绩。

## 项目价值

通过评论识别负面反馈，帮助探索用户体验问题。当前模型只支持英文二分类；不支持中性情绪、中文评论或对个人心理状态的判断。

## 当前状态

- 已审核旧代码，确认硬编码标签、评估标签反转和预处理丢失标签的问题。
- 已准备分步骤 Colab notebook：数据检查 → 基础模型 → DistilBERT → 独立测试 → 错误分析。
- 待实际运行、保存环境版本、填写成绩并展示结果。

旧 `distill-bert.ipynb` 日志记载：Amazon 前 1,000 条样本，80/20 训练验证划分，第三轮验证准确率 93%。这只是历史日志记录，不是本版本独立测试成绩；参考材料中的 92% / 96.22% 也不作为本项目结果。

## 开始

1. 将 `notebooks/01_amazon_sentiment.ipynb` 上传至 Google Colab。
2. notebook 已内嵌数据读取函数，无需额外上传代码文件。
3. notebook 第 1–3 步检查依赖、挂载 Drive、预览 ZIP。确认 ZIP 是无表头的三列 Amazon CSV（标签、标题、评论），标签为 1/2。
4. 按 notebook 顺序继续；DistilBERT 训练使用 Colab GPU。CPU 可以先完成基础模型。
5. 导出 `reports/metrics.json`、混淆矩阵图和 `environment.txt`，审查后提交 GitHub。

原始数据、权重不纳入 Git。Notebook 默认抽样 10,000 条训练来源评论，并抽样 2,000 条独立测试来源评论用于起步实验。抽样结果不能描述为完整测试集成绩。

## 方法

标签映射统一为 `0 = negative`、`1 = positive`。流式随机抽样，标准化空白与 HTML，去重后从训练来源分出分层验证集；测试来源仅用于最终比较。TF-IDF 只在训练集拟合。模型在相同划分上比较 Accuracy、Macro-F1 与混淆矩阵，并保存错误样例供人工阅读。

## 结果（实际运行后填写）

| 模型 | 测试样本数 | Accuracy | Macro-F1 |
|---|---:|---:|---:|
| TF-IDF + Logistic Regression | 待运行 | 待运行 | 待运行 |
| DistilBERT | 待运行 | 待运行 | 待运行 |

## 作品集下一步

完成本项目后，将该仓库链接加入个人主页仓库，补充真实图表、实验设置、失败案例和改进思路。README 中所有数字必须能追溯到运行产物。

## 数据与参考

- Amazon 预期来源：[Amazon Reviews for Sentiment Analysis](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)。Drive 中 ZIP 的来源和许可仍待确认；不得将它与文档提到的其他 Amazon 多属性数据集混为一谈。
- [Hugging Face 文本分类教程](https://huggingface.co/docs/transformers/tasks/sequence_classification)
- [scikit-learn 数据泄漏说明](https://scikit-learn.org/stable/common_pitfalls.html)

此起步版本重新编写实现，没有直接发布 Drive 中来源和许可尚未核实的参考代码。
