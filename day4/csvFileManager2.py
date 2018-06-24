import csv

class CsvFilemanager2:
    @classmethod
    def read(self):
        path=r'C:\Users\51Testing\PycharmProjects\selenium1th\data\test_data.csv'
        file=open(path,'r')
        #通过csv代码库读取打开的csv文件，获取到文件中所有的数据
        data_table=csv.reader(file)


        for item in data_table:
            print(item)

#如果想测试一下这个方法：
if __name__ == '__main__':
   # csvr=CsvFilemanager2()
    #csvr.read()
    #如果在方法上面加上classmethod，表示这个方法可以直接用类调用
   #如果在方法上面加上classmethod，就不需要先实例化对象了
    CsvFilemanager2.read()