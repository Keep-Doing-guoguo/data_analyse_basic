import os.path
import datetime

import pandas as pd
out_path = '/Users/zhangguowen/Library/Mobile Documents/com~apple~CloudDocs/pythonProject2/Kaggle/天池/淘宝用户/data'
path = '/Users/zhangguowen/Library/Mobile Documents/com~apple~CloudDocs/pythonProject2/Kaggle/天池/淘宝用户/tianchi_mum_baby.csv'
path1 = '/Users/zhangguowen/Library/Mobile Documents/com~apple~CloudDocs/pythonProject2/Kaggle/天池/淘宝用户/tianchi_mum_baby_trade_history.csv'

mum_baby = pd.read_csv(path)
trade_history = pd.read_csv(path1)

# 计算订单产生时小孩的天数
# 匹配mum_baby中user_id  对应的trade_history的user_id

tample = mum_baby.merge(trade_history, how="left", on='user_id').fillna(0)#在num_baby的基础之上，在左边进行拼接按照user_id进行拼接。对缺失值填写0。
tample['birthday'] = pd.to_datetime(tample['birthday'].astype(str))#astype只能对pd，series，使用。转换数据类型的。
tample['day'] = pd.to_datetime(tample['day'].astype(str))
age_days = tample['day'] - tample['birthday']#下单时间减去出生时间。下单时间也有可能是怀孕的时间。
a = age_days[0].days
tample.loc[:, 'age_days'] = age_days  # 计算订单产生时小孩的天数。这个是在数据当中新添加一列数据。
j = 0
for i in age_days:
    tample.loc[j,'age_days'] = i.days
    j += 1

tample.age_days = pd.DataFrame(tample.age_days, dtype=int)# age_days为object类型  要改为int类型  不然describe无法统计年龄天数的最值
#tample.describe().to_excel(r'.\result\describe.xlsx')
b = tample.describe()#从describe中可以看到出生年龄最小为负值，最大为10326。可以认为这是异常值，进行删除。
tample[tample['age_days']>2560].sort_values('age_days').to_excel(os.path.join(out_path,'age_days_gt7year.xlsx'))
tample[tample['age_days']<0].sort_values('age_days').to_excel(os.path.join(out_path,'age_days_lt0year.xlsx'))#可以写入到xlsx文件当中。
# 一般认为怀孕了再准备母婴用品会比较常见 这里 我们就以-300天以上为正常  去掉低于-300天的购买数据
tample.drop(tample[tample['age_days'] > 2560].index,inplace=True)#在原始数据上进行操作
tample.drop(tample[tample['age_days'] < -300].index,inplace=True)#删除低于-300的数据

# 查看购买数量   七七八八的加起来50以内还算正常   达到160偏差有点不一般  还是删了吧os.path.join(out_path,'new_trade_history.csv'
tample.sort_values('buy_mount', ascending=False).to_csv(os.path.join(out_path,'new_trade_history.csv'))
tample.drop(tample[tample['buy_mount'] > 50].index, inplace=True)
tample.to_csv(os.path.join(out_path,'new_trade_history.csv'))


#将不使用文件中的数据直接使用已经处理过后的数据
######################二、数据可视化——导入数据和包
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

trade_history = tample
mum_baby_trade_history = pd.read_csv(path1)
######################二、数据可视化——消费者行为分析。通过这个可以分析得出哪一个类别被购买的次数最多。
print(mum_baby_trade_history.groupby('category_1').sum())  # 查看根类别cat1 #[6 rows x 7 columns]
#依次对应的是总数据信息，index=索引信息，values=表格内容信息，aggfunc=表格里面计算的是sum。
result1 = pd.pivot_table(mum_baby_trade_history, index='category_1', values='buy_mount', aggfunc=np.sum)
# plt.figure(figsize=(7, 5))
# plt.bar(x=['28', '38', '50008168', '50014815', '50022520', '122650008'],
#         height=result1['buy_mount'])
# plt.title("category_1 Category sales")
# plt.show()

######################二、数据可视化——不同性别销量情况。通过这个可以得出来哪一个性别更偏向购物。
data = pd.pivot_table(trade_history, index='gender', values='buy_mount', aggfunc=np.sum)
print(data)
# plt.figure(figsize=(5, 5))
# plt.pie(['718', '544', '43'],
#         labels=['female', 'male', 'unknown'],
#         colors=['r', 'b', 'g'],
#         autopct='%.2f%%')#保留的小数位
# plt.title("gender—purchase quantity")
# plt.show()
######################二、数据可视化——消费者行为分析,从这个可以看出来每一个性别对每一个类别的购买数量。
data = pd.pivot_table(trade_history, index='category_1',
                         columns='gender',
                         values='buy_mount',
                         aggfunc=np.sum)
print(data)
#
# plt.figure(figsize=(12,5))
# plt.subplot(221)
# plt.bar(x = ['28', '38', '50008168', '50014815', '50022520', '122650008'],height=data[0],color='r')#性别0对每一个类别的购买数量
# plt.subplot(222)
# plt.bar(x = ['28', '38', '50008168', '50014815', '50022520', '122650008'],height=data[1],color='b')
# plt.subplot(223)
# plt.bar(x = ['28', '38', '50008168', '50014815', '50022520', '122650008'],height=data[2],color='g')
# plt.xlabel("types")
# plt.ylabel("Sales quantity")
# plt.show()
######################二、数据可视化——销量与月份关系.
trade_history = tample
mum_baby_trade_history = pd.read_csv(path1)
mum_baby_trade_history["day"] = mum_baby_trade_history['day'].apply(lambda x:datetime.datetime.strptime(str(x),"%Y%m%d"))
mum_baby_trade_history['Month'] = mum_baby_trade_history.day.astype('datetime64[M]')  # 设置成月份形式,；类型转换。
data_month = mum_baby_trade_history.groupby('Month', as_index=False)  # 按月份分类
df = data_month.buy_mount.sum()  # 新建汇总列表# 按月份汇总
c = mum_baby_trade_history.groupby('Month', as_index=False).sum()['buy_mount']
print(c)
# plt.figure(figsize=(20, 5))#这张图显示的是每一个月份上面的购买数量
# plt.plot(df["Month"], df["buy_mount"])
# plt.show()
######################二、数据可视化——销量与年份关系,可以得知那一年的销量最高。售出的最好。
trade_history = tample
mum_baby_trade_history = pd.read_csv(path1)

mum_baby_trade_history["day"] = mum_baby_trade_history['day'].apply(lambda x: datetime.datetime.strptime(str(x), "%Y%m%d"))
mum_baby_trade_history['Month'] = mum_baby_trade_history.day.astype('datetime64[M]')  # 设置成月份形式
data_month = mum_baby_trade_history.groupby('Month', as_index=False)  # 按月份分类
d = data_month.buy_mount
monthly_buy_mount = data_month.buy_mount.sum()  # 按月份汇总
monthly_user_id = data_month.user_id.sum()#测试使用
e = monthly_buy_mount['Month'][0]
monthly_buy_mount['Year'] = monthly_buy_mount['Month'].dt.year#提取年份，这个dt.year只能对series和datatime的类型的数据使用。
annual_buy_mount = monthly_buy_mount.groupby('Year')['buy_mount'].sum()#按照年份对购买量进行分组并计算总和
annual_buy_mount1 = monthly_buy_mount.groupby('Year').sum()['buy_mount']
# 生成柱状图
# plt.figure(figsize=(10, 5))
# plt.bar(annual_buy_mount.index, annual_buy_mount.values)
# plt.xlabel('Year')
# plt.ylabel('Buy Mount')
# plt.title('Annual Buy Mount')
# plt.show()

######################二、数据可视化——销量与季度关系，哪一个季度淘宝出货量最高。
trade_history = tample
mum_baby_trade_history = pd.read_csv(path1)#这个是原始数据，对原始数据进行改进。
mum_baby_trade_history["day"] = mum_baby_trade_history['day'].apply(lambda x: datetime.datetime.strptime(str(x), "%Y%m%d"))#strptime是用来将str格式转换为时间格式的，后面的字符串需要自己定义。
mum_baby_trade_history['Quarter'] = mum_baby_trade_history.day.dt.quarter  # 添加季度列
mum_baby_trade_history['Year'] = mum_baby_trade_history.day.dt.year  # 添加年份列
#设置as_index=False参数可以确保分组键不会作为索引，而是作为列保留在结果中。
data_quarter = mum_baby_trade_history.groupby(['Year', 'Quarter'], as_index=False)  # 按年份和季度分类
quarterly_buy_mount = data_quarter.buy_mount.sum()  # 按季度汇总
# 生成季度流量柱状图
# plt.figure(figsize=(10, 5))
# x_ticks_labels = [f'Q{q}' for q in quarterly_buy_mount['Quarter']]  # 季度标签，如Q1, Q2, ...
# plt.bar(quarterly_buy_mount.index, quarterly_buy_mount['buy_mount'])
# plt.xticks(quarterly_buy_mount.index, x_ticks_labels)
# plt.xlabel('Quarter')
# plt.ylabel('Buy Mount')
# plt.title('Quarterly Buy Mount')
# plt.show()

######################二、数据可视化——周度流量分析,可以观察到每一周之内用户下单的数量总和
trade_history = tample
mum_baby_trade_history = pd.read_csv(path1)
mum_baby_trade_history['day'] = pd.to_datetime(mum_baby_trade_history['day'], format='%Y%m%d')
mum_baby_trade_history['Week'] = mum_baby_trade_history['day'].dt.isocalendar().week
f = mum_baby_trade_history.groupby('Week', as_index=False).sum()['buy_mount']
data_week = mum_baby_trade_history.groupby('Week', as_index=False)
weekly_buy_mount = data_week.size()

# plt.figure(figsize=(10, 5))
# plt.bar(weekly_buy_mount['Week'], f)
# plt.xlabel('Week')
# plt.ylabel('Buy Mount')
# plt.title('Weekly Buy Mount')
# plt.xticks(rotation=45)
# #plt.subplots_adjust(bottom=0.2)
#
# plt.show()
######################二、数据可视化——用户复购率
trade_history = tample
mum_baby_trade_history = pd.read_csv(path1)
#复购的用户有27个
data_du = mum_baby_trade_history[mum_baby_trade_history.duplicated('user_id')]  # 查看复购数据，重复购买的数据，其user_id一定会重复一遍。

print(data_du.info())
#商品种类复购，
sale_fu = pd.pivot_table(data_du,index='category_1',values='buy_mount',aggfunc=np.sum)
print(sale_fu)#对于这个sale_fu的总和大于27，原因是某一个user_id对某一种商品进行了多次购买。
# plt.figure(figsize=(5,5))
# plt.bar(x=['50014815','38','28','50008168'],
#         height=['2','4','8','19'])
# ax = plt.gca()
# ax.set_xlabel("CATEGORY")
# ax.set_ylabel("sales volume")
# plt.show()

print()
