import collections

with open("modify_data_temp0718_result.txt","r",encoding='utf8') as f:
    data_list = f.readlines()

en_list = []
shu_xing_list = []
shu_xing_zhi_list = []
for data in data_list:
    list1 = data.split(",")
    en = list1[0]
    shu_xing = list1[1]
    shu_xing_zhi = list1[2]
    en_list.append(en)
    shu_xing_list.append(shu_xing)
    shu_xing_zhi_list.append(shu_xing_zhi)

en_dict = dict(collections.Counter(en_list))
shuxing_dict = dict(collections.Counter(shu_xing_list))
shuxingzhi_dict = dict(collections.Counter(shu_xing_zhi_list))
print(en_dict)
# print(shuxing_dict)
# print(shuxingzhi_dict)
f1 = open("实体.txt",'w',encoding='utf8')
f2 = open("属性.txt",'w',encoding='utf8')
f3 = open("属性值.txt",'w',encoding='utf8')


for key1,value1 in en_dict.items():
    f1.write(key1+"   "+str(value1))
    f1.write("\n")
for key2,value2 in shuxing_dict.items():

    f2.write(key2+"   "+str(value2))
    f2.write("\n")
for key3,value3 in shuxingzhi_dict.items():

    f3.write(key3.replace("\n","")+"   "+str(value3))
    f3.write("\n")

f1.close()
f2.close()
f3.close()