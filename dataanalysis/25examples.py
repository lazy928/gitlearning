# -*- coding: utf-8 -*-

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sns
# import warnings; warnings.filterwarnings(action='once')
#
# large = 22
# med = 16
# small = 12
# params = {'axes.titlesize': large,
#           'legend.fontsize': med,
#           'figure.figsize': (16, 10),
#           'axes.labelsize': med,
#           'axes.titlesize': med,
#           'xtick.labelsize': med,
#           'ytick.labelsize': med,
#           'figure.titlesize': large}
# plt.rcParams.update(params)
# plt.style.use('seaborn-whitegrid')
# sns.set_style("white")
#
# # Version
# print(mpl.__version__)  #> 3.0.0
# print(sns.__version__)  #> 0.9.0

# 1 散点图
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")
#
# # Prepare Data
# # Create as many colors as there are unique midwest['category']
# categories = np.unique(midwest['category'])
# colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
#
# # Draw Plot for Each Category
# plt.figure(figsize=(16, 10), dpi=80, facecolor='w',edgecolor='k')
# for i, category in enumerate(categories):
#     plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category==category, :], s=20, c=colors[i], label=str(category))
#
# # Decorations
# plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000), xlabel='Area', ylabel='Population')
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
# plt.legend(fontsize=12)
# plt.show()

# 2 带边界带气泡图
# import seaborn as sns
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.spatial import ConvexHull
# import warnings; warnings.simplefilter('ignore')
# sns.set_style("white")
#
# midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")
#
# # As many colors as there are unique midwest['category']
# categories = np.unique(midwest['category'])
# colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
#
# # Draw Scatterplot with unique for each category
# plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
# for i, category in enumerate(categories):
#     plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category==category, :], s='dot_size', c=colors[i], label=str(category), edgecolor='black', linewidths=0.5)
#
# # Encircling
# # https://stackoverflow.com/questions/44575681/how-do-i-encircle-different-data-sets-in-scatter-plot
# def encircle(x, y, ax=None, **kw):
#     if not ax: ax=plt.gca()
#     p = np.c_[x, y]
#     hull = ConvexHull(p)
#     poly = plt.Polygon(p[hull.vertices, :], **kw)
#     ax.add_patch(poly)
#
# # Select data to be encircled
# midwest_encircle_data = midwest.loc[midwest.state=='IN', :]
#
# # Drew polygon surrounding vertices
# encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="k", fc="gold", alpha=0.1)
# encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="firebrick", fc="none", linewidth=1.5)
#
# # Decorations
# plt.gca().set(xlim=(0, 0.1), ylim=(0, 90000), xlabel='Area', ylabel='Population')
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.title("Bubble Plot with Encircling", fontsize=22)
# plt.legend(fontsize=12)
# plt.show()

# 3 带线性回归最佳拟合线带散点图(有瑕疵)
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
# df_select = df.loc[df.cyl.isin([4, 8]), :]
#
# # plot
# sns.set_style("white")
# gridobj = sns.lmplot(x='displ', y='hwy', data=df_select, height=7, robust=True, palette='Set1', col='cyl', scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
#
# # Decorations
# gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
# # plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=10)
# plt.show()

# 4 抖动图
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
#
# fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
# sns.stripplot(df.cty, df.hwy, jitter=0.25, size=8, ax=ax, linewidth=.5)
# plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
# plt.show()

# 5 计数器(有错误)
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
# df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')
# fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
# sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts*2, ax=ax) #报错
# plt.title('Counts plot - Size of circle is bigger as more points overlap', fontsize=22)
# plt.show()

# 6 边缘直方图(问题同上)
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
#
# fig = plt.figure(figsize=(16, 10), dpi=80)
# grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)
#
# # Define the axes
# ax_main = fig.add_subplot(grid[:-1, :-1])
# ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
# ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])
#
# # Scatterplot on main ax
# ax_main.scatter('displ', 'hwy', s=df.cty*4, c=df.manufacturer.astype('category').cat.codes, alpha=.9, data=df, cmap="tab10", edgecolors='gray', linewidths=.5)
#
# # histogram on the right
# ax_bottom.hist(df.displ, 40, histtype='stepfilled', orientation='vertical', color='deeppink')
# ax_bottom.invert_yaxis()
#
# # histogram in the bottom
# ax_right.hist(df.hwy, 40, histtype='stepfilled', orientation='horizontal', color='deeppink')
#
# ax_main.set(title='Scatterplot with Histograms displ vs hwy', xlabel='displ', ylabel='hwy')
# ax_main.title.set_fontsize(20)
# for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
#     item.set_fontsize(14)
#
# xlabels = ax_main.get_xticks().tolist()
# ax_main.set_xticklabels(xlabels)
# plt.show()

# 7 边缘箱型图
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
#
# fig = plt.figure(figsize=(16, 10), dpi=80)
# grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)
#
# ax_main = fig.add_subplot(grid[:-1, :-1])
# ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
# ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])
#
# ax_main.scatter('displ', 'hwy', s=df.cty*5, c=df.manufacturer.astype('category').cat.codes, alpha=.9, data=df, cmap="Set1", edgecolors='black', linewidths=.5)
#
# sns.boxplot(df.hwy, ax=ax_right, orient="v")
# sns.boxplot(df.displ, ax=ax_bottom, orient="h")
#
# # remove x axis name for the boxplot
# ax_bottom.set(xlabel='')
# ax_right.set(ylabel='')
# ax_main.set(title='Scatterplot with Histograms displ vs hwy', xlabel='displ', ylabel='hwy')
# ax_main.title.set_fontsize(20)
# for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
#     item.set_fontsize(14)
#
# plt.show()

# 8 相关图
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
#
# plt.figure(figsize=(12, 10), dpi=80)
# sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
#
# plt.title('Correlogram of mtcars', fontsize=22)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.show()

# 9 矩阵图
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
# plot 1
# plt.figure(figsize=(10, 8), dpi=80)
# sns.pairplot(df, kind='scatter', hue='species', plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
# plt.show()

# plot 2
plt.figure(figsize=(10, 8), dpi=80)
sns.pairplot(df, kind='reg', hue='species')
plt.show()

# 10 发散型条形图
