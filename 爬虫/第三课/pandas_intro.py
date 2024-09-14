import pandas as pd

#创建表格步骤
#1.创建dataframe对象
#2.将dataframe对象转化为表格

#如果传入列表，列表里每个元素是一个字典，那么就是
#则是按照行来创建列表
# df = pd.DataFrame(
#     [
#         {"aaa":123,"bbb":444},
#         {"aaa":555,"bbb":666}
#     ]
# )

# df.to_excel("output1.xlsx")

#按照列创建表格,传入字典，每个键值对是一列
df = pd.DataFrame({
    "name":[1,2,3],
    "age":[4,5,6],
    "salary":[9,7,8]
})
# df.to_excel("output3.xlsx",index=False)
df.to_excel("output5.xlsx",header=False,sheet_name="hhh")