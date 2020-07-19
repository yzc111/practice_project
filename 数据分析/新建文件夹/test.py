class Sale:

    def __init__(self,bill_number,goods_num,goods_name,goods_number,bill_data,per_price,customer_num,country):
        self.bill_number = bill_number
        self.goods_num = goods_num
        self.goods_name = goods_name
        self.goods_number = goods_number
        self.bill_data = bill_data
        self.per_price = per_price
        self.customer_num = customer_num
        self.country = country



data_list = []
with open("1个月的销售数据(1).txt",'r',encoding = 'gbk') as f:
    data = f.read()



data = data.split('\n')
col = data[0].split(',')

dict1 = {}
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []


data = data[1:]
data_detail_list = []
for i in range(len(data)):
    data_detail_list.append(data[i].replace("\n","").split(','))
sale_list = []

for data in data_detail_list:

    try:
        data[3] = int(data[3])
        if data[3] > 0:
            try:
                data[5] = float(data[5])

                if data[5] != 0  and data[5] > 0:
                    if data[6]:
                        list1.append(data[0])
                        list2.append(data[1])
                        list3.append(data[2])
                        list4.append(data[3])
                        list5.append(data[4])
                        list6.append(data[5])
                        list7.append(data[6])
                        list8.append(data[7])
                        sale_obj = Sale(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
                        sale_list.append(sale_obj)




            except:
                pass
    except:
        pass




#客户数目
consumer_number = len(set(list7))
#产品数目
goods_count = len(set(list2))
#发票数目
bill_number_count = len(set(list1))
#国家数目
country_number = len(set(list8))
#销售数量
goods_sale_number_count = 0
for i in list4:
    goods_sale_number_count += i

#赋初值,用来保存最大值和最小值以及对应的信息
dict1 = {
    "max_price":sale_list[0].per_price,
    "goods_num":sale_list[0].goods_num
        }

dict2 = {
    "min_price":sale_list[0].per_price,
    "goods_num":sale_list[0].goods_num
        }

price_count = 0
con_set = set(list7)
# print(con_set)
for sale_data in sale_list:
    price_count += (sale_data.per_price*sale_data.goods_number)


    if dict1['max_price'] < sale_data.per_price:
        dict1['max_price'] = sale_data.per_price
        dict1['goods_num'] = sale_data.goods_num

    if dict2['min_price'] > sale_data.per_price:
        dict2['min_price'] = sale_data.per_price
        dict2['goods_num'] = sale_data.goods_num
# print(list7)
dict3 = {}
for con in con_set:
    dict3[con] = 0
    for sale_data in sale_list:
        if sale_data.customer_num == con:
            sum = sale_data.per_price * sale_data.goods_number
            # print(round(sum,2))
            dict3[con] = round(sum,2)



list0 = []
for key,value in dict3.items():
    list0.append(round(value,2))

print(dict3)
list0.sort()

length = len(list0)
persent = int(length * 0.1)

top_10_persent = list0[-130:]
bottom_10_persent = list0[:130]

print(top_10_persent)




con_10_persent_list_top = []
top_sum = 0
bottom_sum = 0
for i in top_10_persent:
    top_sum += i
for i in bottom_10_persent:
    bottom_sum += i
con_10_persent_list_bottom = []
for key,value in dict3.items():

    for i in top_10_persent:

        if value == i:
            con_10_persent_list_top.append(key)

    for i in bottom_10_persent:

        if value == i:
            con_10_persent_list_bottom.append(key)

print(set(con_10_persent_list_bottom))
print(round(bottom_sum,2))
print(set(con_10_persent_list_top))
print(round(top_sum,2))
with open('result.txt','w',encoding='utf8') as f:
    str1 = "客户数目    产品数目   发票数目   国家数目    销售数量"
    str2 = str(consumer_number)+"      "+str(goods_count)+"      "+str(bill_number_count)+"      "+str(country_number)+"      "+str(goods_sale_number_count)
    str3 = "消费最高的10%客户编号：" + str(set(con_10_persent_list_top))
    str4 = "消费最高的10%客户的消费总额："+str(round(top_sum,2))
    str5 = "消费最低的10%客户编号：" + str(set(con_10_persent_list_bottom))
    str6 = "消费最低的10%客户的消费总额：" + str(round(bottom_sum,2))
    f.write(str1)
    f.write('\n')
    f.write(str2)
    f.write('\n')
    f.write(str3)
    f.write('\n')
    f.write(str4)
    f.write('\n')
    f.write(str5)
    f.write('\n')
    f.write(str6)



