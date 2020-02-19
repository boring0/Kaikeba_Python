Day_Num_All= []
for Sum_New in range(1,8):
    print("请输入第%s天收入:"% Sum_New)
    Day_Num = int(input())
    Day_Num_All=Day_Num_All+[Day_Num]
Day_Num_All_Less=int()
for Less_New in range(1,8):
    print("请输入第%s天支出:" % Less_New)
    Day_Num_Less = int(input())
    Less_New_De=Less_New-1
    Day_Num_De=Day_Num_All[Less_New_De]-Day_Num_Less
    Day_Num_All_Less=Day_Num_All_Less+Day_Num_De
    print("第%s天结余:%s"% (Less_New,Day_Num_De))
print("当前总结余:%s"% Day_Num_All_Less)