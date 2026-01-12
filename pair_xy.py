import matplotlib 
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20) 
matplotlib.rc('font', family='Arial')
import matplotlib.pyplot as plt

from pyplotz.pyplotz import PyplotZ
pltz = PyplotZ()
pltz.enable_chinese()


# 假設的VPN速度數據 (單位：Mbps)
data = {
    "上海": {"上海": 0, "香港": 50, "台灣": 40, "日本": 30},
    "香港": {"上海": 55, "香港": 0, "台灣": 60, "日本": 45},
    "台灣": {"上海": 35, "香港": 65, "台灣": 0, "日本": 50},
    "日本": {"上海": 30, "香港": 45, "台灣": 55, "日本": 0}
}

df = pd.DataFrame(data)
# 繪製熱圖
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap="coolwarm", fmt="d")
plt.title("VPN速度熱圖 (Mbps)")
plt.xlabel("目的地")
plt.ylabel("來源地")
plt.show()