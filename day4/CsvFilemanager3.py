import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个csv文件，所以每次也应该关闭该文件
class CsvFilemanager3:
    @classmethod
    def read(self):
        path=r'C:\Users\51Testing\PycharmProjects\selenium1th\data\test_data.csv'
        file=open(path,'r')
        try:   #try尝试执行以下代码
            #通过csv代码库读取打开的csv文件，获取到文件中所有的数据
            data_table=csv.reader(file)

    #如何保证，不论程序执行过程中是否报错，都能正常关闭打开的文件
            for item in data_table:
                print(item)



                #方法最后应该添加close（）方法
        finally:  #finally最终，不论过程是否报错，都会执行以下代码
            file.close()

#如果想测试一下这个方法：
if __name__ == '__main__':
   # csvr=CsvFilemanager2()
    #csvr.read()
    #如果在方法上面加上classmethod，表示这个方法可以直接用类调用
   #如果在方法上面加上classmethod，就不需要先实例化对象了
    CsvFilemanager3.read()