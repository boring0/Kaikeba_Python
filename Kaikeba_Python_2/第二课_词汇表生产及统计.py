# coding=gbk
#text = '2019 �� ʮ�� һ�� ���� �� ��ף �л����񹲺͹� ���� 70 ���� �ı�ʽ �� �׶����� ʢ����� �� 59 �� �ı� ���� �� 580 ̨�� �� װ�� �� 1.5 ���� �� ���� ���� ���� �� ȫ�� ���� �� ���� �� �ı� װ�� ���� չʾ �� ����װ�� �� Ϊ ���� ���� ��ս װ�� �� 40% Ϊ �״� չʾ �� ���� ��Щ���� ���� ȫ�� ��ע �� ���� 41 �޼� �������� �� ���� ��Ǳ�� �������� �� ���� 17 �߳����� ���� ϵͳ ���� ��Ļ ���� �� �� " ��ŭ ���� " �� ���� �� ���� չʾ �й� ���� ��ƽ �� ��־ �� ���� �� ��� �� ���� �׶� ���� ���� �� ����װ�� �� �� ���� ���� ���� �� ���� ���� �� ���� ��ע �� �� �� �� " ��� ��ʯ " �� ��λ �� �� ���� ���� ���� �� �ڴ� �� �� ���� ����װ�� ʵ�� ���� ��� �� �� ���� �е� �� ���� �� ��ʷ " ʹ�� " �� �� ���� ��Լ ��� ���� ���� ר�� �� Ϊ ��� ��ϸ ��� �� ���� ���� ���� �� �� ���� �� �� ֮ ���� ��'
text = input()
Name_All = []
Name_De=''
Name_Sum=0
Name_All_Word2Id = dict()
Name_All_Id2Word = dict()
for name in text:
    if name == ' ':
        Name_All=Name_All+[Name_De]
        Name_De=''
    else:
        Name_De=Name_De+name
Name_All_read = set()
for Name_All_De in Name_All:
    Name_All_read.add(Name_All_De)
for Name_All_Word in Name_All_read:
    Name_All_Word2Id[Name_All_Word]=Name_Sum
    Name_All_Id2Word[Name_Sum]=Name_All_Word
    Name_Sum=Name_Sum+1
print(Name_All_read)
print(Name_All_Word2Id)
print(Name_All_Id2Word)