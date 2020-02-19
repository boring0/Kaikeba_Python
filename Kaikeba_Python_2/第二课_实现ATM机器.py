import random
User_Sum_Num=random.randint(1300,2620)
Quit_Num=0
while Quit_Num == 0:
    print("请选择您要的功能:\n\t1、查询余额\n\t2、存款\n\t3、取款\n\t4、退出")
    Mess_All= int(input())
    if Mess_All == 1:
        print("您当前余额为:%s"%User_Sum_Num)
    elif Mess_All == 2:
        print("请输入需存款金额:")
        User_Sum_Num_New=int(input())
        User_Sum_Num = User_Sum_Num + User_Sum_Num_New
    elif Mess_All == 3:
        print("请输入需取款金额:")
        User_Sum_Num_De=int(input())
        User_Sum_Num = User_Sum_Num - User_Sum_Num_De
    elif Mess_All == 4:
        Quit_Num=1