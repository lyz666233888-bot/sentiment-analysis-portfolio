# 项目审核与学习路线

审核日期：2026-10-13。范围：用户指定 Drive 文件夹的 13 个文件；已读取 README、4 个 Python 脚本、2 个 notebook 和数据说明，实际读取 imdb_train.csv。ZIP 内部与 imdb_test.csv 尚未核对。

## 已核实的发现

| 文件 | 发现 | 后续处理 |
|---|---|---|
| imdb_train.csv | CSV 实际为 100 行，仅 review 列 | 不从行号自动生成标签 |
| split_data.py | 只取各类别 50 条，并导出时删除 sentiment | 从带标签源重新生成数据 |
| run_imdb.py / run_amazon.py | 标签固定为前 50 条 1、后 50 条 0；evaluate 的标签反向 | 逐行保留标签，评估用数据真实标签 |
| run_imdb.py / run_amazon.py | 手动使用 CLS/SEP，未传 attention mask；predict 调用缺 tokenizer；导入即训练 | 使用 tokenizer 标准接口，训练单独执行 |
| read_amazon.py | 从测试来源切训练/测试；丢弃标签；追加写入可能重复 | 读取原训练与测试来源，保留标签 |
| distill-bert.ipynb | 有保存的训练输出，前 1,000 条，第三轮验证 93%；无独立测试评估 | 保留历史记录，随机抽样、分层验证、独立测试 |
| Amazon 参考 notebook | TF-IDF 在划分前 fit；使用 2020 nightly Torch；预测引用未定义 plain_model；96.22% 仅正文宣称 | 重新实现 pipeline，核验实际运行结果 |
| README.md | 命令引用不存在的 script.py / read-amazon.py，与文件名不一致 | 使用 notebook 实际步骤 |
| Sentiment dataset.docx | Amazon 描述与代码使用的 polarity 数据格式不同 | 核对 ZIP 来源、格式与许可 |

## 每次只完成一个学习关卡

1. **数据检查**：能说明输入格式、样本数、标签含义、训练与测试来源。先运行新 notebook 的第 1–3 步，将 ZIP 文件名和前 5 条的标签输出带回聊天（无需粘贴完整评论）。
2. **基础模型**：理解 TF-IDF 与 Logistic Regression；生成验证 Accuracy / Macro-F1。确认训练和验证无重复。
3. **DistilBERT**：理解 tokenizer、attention mask、epoch、学习率；训练并保存验证表现最好的 checkpoint。
4. **最终比较**：用同一份此前未参与调参的独立测试样本评估两模型，保存环境和指标。后续若根据测试成绩调参，需要新的最终评估集。
5. **错误分析**：手工分类至少 20 条误判，例如否定、讽刺、长评论、多方面混合意见。由实际样例得出结论。
6. **GitHub 展示**：补齐 README 结果与真实图表，将项目链接放入个人主页，准备简历描述和面试讲解。

## GitHub 建议

仓库名：sentiment-analysis-portfolio。初始状态写明进行中。只提交重新编写的代码、清理输出的 notebook 和已审核的报告；原始数据与模型保留在 Drive。个人主页仓库使用 GitHub 实际用户名同名仓库。已确认用户登录 GitHub，开始搭建作品集。
