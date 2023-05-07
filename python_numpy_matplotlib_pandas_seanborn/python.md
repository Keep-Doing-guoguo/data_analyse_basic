# 1.Python
# 1.1内置函数
Python中的内置函数是指在Python解释器启动时就已经加载到内存中的函数，不需要额外的导入就可以直接使用。
### print() 输出内容到控制台。
### round()：对对象进行四舍五入。
### abs() 绝对值
### max() 最大值
### min() 
### sum()
### sorted()
### set()
### dict()
### list()
### float()
### len()
### range()
### str()
# 1.2属性
这些属性是 Python 内置属性，可以被任意的对象调用和使用。
### __name__ 模块名或者函数名
### __doc__  文档字符串
### __class__类名
### __bases__基类元组
### __dict__ 类或实例的属性
### __module__定义该类或函数的模块名称
### __file__ 定义该类或函数的文件名称
# 2.math
### math.ceil(x)：返回大于等于 x 的最小整数。
### math.floor(x)：返回小于等于 x 的最大整数。
### math.sqrt(x)
### math.exp(x)
### math.log(x)
### math.log10(x)
### math.sin(x)
### math.cos(x)
### math.tan(x)
### math.asin(x)
### math.acos(x)
### math.atan(x)
### math.trunc(x)
### math.factorial(x)
### math.fmod(x, y) 方法返回 x/y 的余数。

# 2.Seaborn
1.sns.boxplot()#绘制箱型图，可以观察到异常值。    
2.sns.histplot()绘制直方图，需要bins。  
3.heatmap绘制热力图。斯皮尔曼相关系数。通常用于探索数据集中的变量之间的相关性。  
`sns.heatmap(numeric_feature.corr('spearman'),annot=True,fmt='g',cmap='Blues')`
4.countplot对数据中的某一特征进行计数，并且画图显示。
5.argsort()排序之后，返回的是索引。  
6.sns.pairplot()用来展示两两特征之间的关系，通常用于探索数据集中的变量之间的关系和分布。  
relplot()：用于绘制关系图，包括散点图、线图等等。  
catplot()：用于绘制分类图，包括柱状图、箱线图等等。  
distplot()：用于绘制直方图和密度图。  
jointplot()：用于绘制两个变量之间的关系图，包括散点图、回归线、相关系数等等。  
lmplot()：用于绘制线性回归模型，通常用于探索两个变量之间的线性关系。  
swarmplot()：用于绘制分布图，通常用于探索类别变量和数值变量之间的关系。  
boxplot()：用于绘制箱线图，通常用于探索数值变量的分布情况和离群值。  
violinplot()：用于绘制小提琴图，通常用于探索数值变量的分布情况和离群值。  






# 3.Pandas
## 3.1方法
1.concat([a,b])拼接操作
2.groupby()分组操作
sum：是用来求和的  
agg：
`data.groupby('State').agg({'Yield':'max'})`取出来Yield这一个特征的最大值
3.
`pd.set_option('display.max_rows', 200)`  
`pd.set_option('expand_frame_repr', False)`
4.
3.merge()合并操作
4.quantile()表示分位数的意思，一般为0.25,0.5,0.75。分位数。  
5.get_dummies()表示将使用哑变量。sklearn中的onehotencoder一样的效果。  
6.检查缺失值  
`data.info()`  
`data.isnull().sum()`

7.nunique()输出的是unique的数目  
8.unique()输出的是单一的值  
9.dropna()删除null值  
10.nlargest()选择最大值，numpy也可以使用。  
11.sort_values(ascending=False)ascending指的是上升的意思，为True就是。  
12.drop_duplicates()删除重复的值  
13.Dataframe中的value_counts()对种类进行分别计数。
`pd.to_datatime(df['arrival_year'].astype(str)+df['arrival_month'].astype(str),format='%Y%m')`  
14.dropna(axis=0)将这一行其中有null的数据删除掉。对于少部分有null值的可以如何处理。15.to_csv()将数据保存到本地文件。  
replace()：将DataFrame或Series对象中的指定值替换为其他值。  
astype()：将DataFrame或Series对象的数据类型转换为指定类型。  
loc[]：基于标签选择行和列。  
iloc[]：基于位置选择行和列。  
set_index()：将DataFrame对象的列设置为索引。  
reset_index()：将DataFrame对象的索引重置为默认的数字索引。  
drop_duplicates()：从DataFrame中删除重复的行。  
value_counts()：返回DataFrame中每个唯一值的数量。
## 3.2属性
Series.index：返回数据的索引，类型为 Index。  
Series.name：返回 Series 的名称。  
DataFrame.index：返回数据的行索引，类型为 Index。  
DataFrame.columns：返回数据的列索引，类型为 Index。  
DataFrame.values：返回数据的值，类型为 ndarray。  
DataFrame.dtypes：返回每列数据的数据类型，类型为 Series。  
DataFrame.shape：返回数据的形状，即 (行数, 列数)，类型为元组。  
DataFrame.size：返回数据的大小，即行数与列数的乘积。  
DataFrame.ndim：返回数据的维度，Series 为 1，DataFrame 为 2。  
DataFrame.T：返回数据的转置。  
DataFrame.axes：返回行和列索引的标签列表，以元组的形式给出，如 (Index(['a', 'b', 'c']), Index(['A', 'B', 'C']))。  
DataFrame.empty：返回数据是否为空，如果为空则返回 True。  
DataFrame.iat：返回指定行列位置的值，类型为标量值。  
DataFrame.at：返回指定行列标签的值，类型为标量值。





# 4.Mataplotlib
## 4.2方法
### 1.一图多个的画法操作
这是第一种  
`plt.figrue()`  
`plt.plot()`  
`plt.show()`  
这是第二种  
`plt.figure()`  
`plt.subplot(1,3,1)`  
`sns.histplot()`  
`plt.subplot(1,3,2)`  
`sns.boxplot()`  
`plt.subplot(1,3,3)`  
`plt.plot()`  
这是第三种  
`fig,axs = plt.subplots(1,3)`  
`axs[0].`  
`axs[1].`
1.plot()：绘制线图  
2.scatter()：绘制散点图  
3.bar()：绘制柱状图  
4.hist()：绘制直方图  
5.boxplot()：绘制箱线图  
6.pie()：绘制饼图  
7.imshow()：绘制图像  
8.contour()：绘制等高线图  
9.quiver()：绘制矢量图  
10.streamplot()：绘制流线图  
11.errorbar()：绘制误差线图  
12.fill_between()：绘制填充曲线  
13.text()：绘制文本  
## 4.2属性
xlabel()：设置x轴标签  
ylabel()：设置y轴标签  
title()：设置图表标题  
legend()：设置图例  
xlim()：设置x轴范围  
ylim()：设置y轴范围  
grid()：显示网格线  
xticks()：设置x轴刻度  
yticks()：设置y轴刻度  






# 5.Numpy
## 5.1Numpy的方法
1.np.where(condition,x,y)当where内有三个参数时，第一个参数表示条件，当条件成立时where方法返回x，当条件不成立时where返回y  
2.np.bincount()将其从小到大进行排序，然后对每一个数值进行技术，并且返回技术结果的函数。  
3.np.argmax()是找到array中最大值，并且返回最大值索引的函数。  
4.np.floor()只保留小数的整数部分。  
5.np.ceil()向上取整  
6.np.full（）创建一个全部都是一个数字的矩阵。  
7.np.clip（）设置一个上下界。  
8.np.fliplr()将数组将数组从左向右翻转  
9.np.ceil()取整函数  
10.np.argsort()返回的是元素值从小到大排序后的索引值的数组  
11.数组创建：array, zeros, ones, empty, arange, linspace, random  
12.数组形状：reshape, resize, stack, hstack, vstack  
13.数组操作：split, repeat, tile, delete, insert, append, unique  
14.数组运算：add, subtract, multiply, divide, sqrt, exp, log, sin, cos, tan, dot, inner, outer, transpose, sum, mean, std, max, min, argmax, argmin  
## 5.2Numpy的属性
1.ndarray.ndim：返回数组的维度数。  
2.ndarray.shape：返回一个包含数组各维度大小的元组。  
3.ndarray.size：返回数组元素总数。  
4.ndarray.dtype：返回数组元素的数据类型。  
5.ndarray.itemsize：返回数组每个元素的字节大小。  
6.ndarray.nbytes：返回数组总字节大小。  


# 6.os
1.os.listdir()  
2.os.path.join()  
3.os.path.isdir()  
4.os.path.exists()  
5.os.rename()  
6.os.getcwd()  
7.os.makedirs()  

# 7.opencv2

1.cv2.imraed()读取图片操作  
2.cv2.blur()增加模糊程度  
3.cv2.resize()改变图片大小  
4.cv2.cvtColor()更换BGR或者RGB或者HSV的图片格式  
5.cv2.merge()对通道进行合并  

# 8.pytorch
1.expand_as()扩展张量，使得和原来张量大小相同。  