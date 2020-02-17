import numpy as np
import seaborn as sns
# ROC与PR实现
"""
       混淆矩阵介绍
|        |    预测结果
|真实情况    正例    反例
|  正例   TP真正例 FN假反例
|  反例   FP假正例 TN真反例

查准率=TP/(TP+FP)
查全率(真正例率)=TP/(TP+FN)
真反例率=TN/(FP+TN)

"""


# 生成样本集


