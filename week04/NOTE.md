Pandas
=====
Python中的Excel，潘大师
sklearn数据集可供学习使用
```python
from sklearn import datasets
iris = datasets.load_iris()
#load_boston() load_digits()

import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv(book) #DataFrame
print(df)
df[0:3]
df.columns = ['star','vote','shorts']  #加表头
df.['start'] == '力荐'     #返回True False
df.[df.['start'] == '力荐']
df.dropna()    #缺失数据删除
df.groupby('start').sum()

#创建新列
start_to_number={
                 '力荐':5,
				 '推荐':4,
				 '还行':3
				}
df['new_star'] = df['star'].map(start_to_number)
```

Pandas两个数据类型
======
Series
------
excel中列，有索引


DataFrame
-----------
多行多列，excel

Pandas数据导入
======
read_*()  read_excel(r'1.xlsx')#pip install xlrd  
          read_sql(sql,conn)
		  read_csv(r'c:\file.csv',sep=' ',nrows=10,encoding='utf-8')
		  read_table(r'file.txt',sep=' ')
		  
```python
import pymysql
sql='select * from mytable'
conn=pymysql.connect('ip','name','pass','dbname','charset=uft8')
df=pd.read_sql(sql.conn)
```

Pandas数据预处理
======
```python
x=pd.Series([,,])
x.hasnans   #是否存在缺失
x.fillna(value=x.mean())

df3=pd.DataFrame()
df3.isnull()
df3.isnull().sum()

df3.fill()  #上一行填充缺失
df3.fill(axis=1)  #前一行填充

df3.info()  #显示有多少非空数值
df3.dnpna()  #有缺失值的行删除
df3.fillna('无')  #填充缺失值
df3.drop_duplicates()  #删除重复值

```
Pandas数据调整
======
```python
df[['A','C']]  #列的选择，参数为列表
df.iloc[:,[0,2]]  #：表示所有航，[0,2]第1和第3列

df.loc[[0,2]]  #行的选择，第1和第3行
df.loc[0:2]    #第1到第3行

df['c'].replace(4,40)  #替换，原有的df不变，需要保存
df.T  #转置
df.T.T
```
数据透视表简单来说就是把明细表进行分类汇总的过程，你可以按照不同的组合方式进行数据计算。按不同维度得到想要数据
df4.stack()  df4.unstack()  df4.stack().reset_index()

Pandas基本操作
======
两列之间可以加减乘除进行运算
空值不参与，比较也不参与(False)，所以要清理数据
df.count()  df.sum()  df['A'].sum()
.mean()  .max()  .min()  .median()  .mode()  .var()方差  .stc()标准差  常用函数查文档

Pandas分组聚合
======
groupby  aggregate
  transform


Pandas输出和绘图
======
编码
linux/mac ==>utf-8  win==>GBK
```python
df.to_excel(excel_writer=r'file.xlsx',sheet_name='sheet1',index=False,columns=['col1','col2'])
encoding='utf-8'
na_rep=0  #缺失值填充
df.to_csv()
df.to_pickle('xx.pkl')
#csv有良好的阅读性，pickle有良好性能，约为excel10倍
#agg(sum)快  agg(lambda x:s.sum())慢

import matplotlib.pyplot as plt
plt.plot(df.index,df['A'],color='#00000',linstyle='--',linewidth=3,marker='D')
plt.show()

import Seaborn as sns     #美化plt
sns.set_style('darkgrid')
plt.scatter(df.index,df['A'])
plt.show()
```

jieba分词与提取关键词
======
```python
import jieba
import jieba.analyse

result=jieba.cut(string,cut_all=False)#False精确模式，True全模式（搜索引擎用）

#用户字典，匹配调整
#   词内容        权重   词性
# Python训练营     3      nt
user_dict=r'user_dict.txt'
jieba.load_userdict(user_dict)
jieba.add_word('自定义词')

#合并
jieba.suggest_freq('中出',True)
jieba.suggest_freq(('中','将'),True)
```

SnowNLP情感倾向分析
======
```python
from snownlp import SnowNLP
s=SnowNLP(text)
s.words   #中文分词['','','']
list(s.tags)  #词性
s.sentiments  #评分  0-->1 正向

#SnowNLP用购物数据训练
#换新数据训练
from snownlp import seg
seg.train('data.txt')
seg.save('seg.marshal')
#修改snownlp /seg/_init_.py 的data_path指向

```