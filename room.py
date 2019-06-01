from naverWeather import *

L1 = list()
L2 = list()
L3 = list()

class room():
    def room_1():
        while(1):
            print("-------------------------------------------------------------------")
            print("                        <<< 상의 코너 >>>                        ")
            print("1번 : 옷 추가하기 | 2번 : 옷 삭제하기 | 3번 : 확인하기 | 4번 : 종료")
            print("-------------------------------------------------------------------")
            room1 = input()
            if room1 == '1':
                i = 0
                print("------------------------")
                print("   옷을 입력해주세요.   ")
                print("색갈과 긴/반 을 꼭 입력해주세요")
                print("------------------------")
                L1.insert(i, str(input("")))
            elif room1 == '2':
                print("----------------------------------")
                print("아래 목록에서 삭제할 옷을 고르시오")
                print(L1)
                print("삭제할 옷은?")
                print("----------------------------------")
                a = str(input())
                if a in L1:
                    L1.remove(a)
                    print("삭제되었습니다~")
                else:
                    print("<<<<<<<<<입력한 옷이 없습니다.>>>>>>>>>")
                    print("<<<확인하시고 다시 입력부탁드립니다.>>>")
            elif room1 == '3':
                print(L1)
            elif room1 == '4':
                break
            else:
                print("<<<<<<잘못입력하셨습니다. 다시입력해주세요>>>>>>")
                print("")
    def room_2():
        while(1):
            print("-------------------------------------------------------------------")
            print("              <<< 하의 코너 >>>              ")
            print("1번 : 옷 추가하기 | 2번 : 옷 삭제하기 | 3번 : 확인하기 | 4번 : 종료")
            print("-------------------------------------------------------------------")
            room1 = input()
            if room1 == '1':
                i = 0
                print("----------------------------")
                print("     옷을 입력해주세요.     ")
                print("색갈과 긴/반 을 꼭 입력해주세요")
                print("----------------------------")
                L2.insert(i, str(input()))
            elif room1 == '2':
                print("----------------------------------")
                print("아래 목록에서 삭제할 옷을 고르시오")
                print(L2)
                print("삭제할 옷은?")
                print("----------------------------------")
                b = str(input(""))
                if a in L2:
                    L2.remove(b)
                    print("삭제되었습니다~")
                else:
                    print("<<<<<<<<<입력한 옷이 없습니다.>>>>>>>>>")
                    print("<<<확인하시고 다시 입력부탁드립니다.>>>")
            elif room1 == '3':
                print(L2)
            elif room1 == '4':
                break
            else:
                print("<<<<<<잘못입력하셨습니다. 다시입력해주세요>>>>>>")
                print("")
    def support(self):
         a = list(naverWeather(self).support_1())
         print("\n[[조합결과]]")
         if('26.0' < a[13]):
             cody1 = list(set([s for s in L1 if "나시티" in s] + [s for s in L1 if "민소매" in s] + [s for s in L1 if "반" in s])) #상의 조건결과
             cody2 = list(set([s for s in L2 if "반" in s])) #하의 조건결과
             (s for s in cody2 if "청" in s) # 하의에 "청"이 있으면
             cody3 = list(set([s for s in cody2 if "청" in s])) # "청"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "회" in s) # 상의에 "회"이 있으면
             cody4 = list(set([s for s in cody1 if "회" in s])) # "회"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
         elif('22.0' < a[13] <= '26.0'):
             cody1 = list(set([s for s in L1 if "나시티" in s] + [s for s in L1 if "민소매" in s] + [s for s in L1 if "반" in s])) #상의 조건결과
             cody2 = list(set([s for s in L2 if "반" in s])) #하의 조건결과
             (s for s in cody2 if "청" in s) # 하의에 "청"이 있으면
             cody3 = list(set([s for s in cody2 if "청" in s])) # "청"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "회" in s) # 상의에 "회"이 있으면
             cody4 = list(set([s for s in cody1 if "회" in s])) # "회"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
         elif('19.0' < a[13] <= '22.0'):
             cody1 = list(set([s for s in L1 if "나시티" in s] + [s for s in L1 if "민소매" in s] + [s for s in L1 if "반" in s])) #상의 조건결과
             cody2 = list(set([s for s in L2 if "반" in s])) #하의 조건결과
             (s for s in cody2 if "청" in s) # 하의에 "청"이 있으면
             cody3 = list(set([s for s in cody2 if "청" in s])) # "청"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "회" in s) # 상의에 "회"이 있으면
             cody4 = list(set([s for s in cody1 if "회" in s])) # "회"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
         elif('17.0' < a[13] <= '19.0'):
             cody1 = list(set([s for s in L1 if "나시티" in s] + [s for s in L1 if "민소매" in s] + [s for s in L1 if "반" in s])) #상의 조건결과
             cody2 = list(set([s for s in L2 if "반" in s])) #하의 조건결과
             (s for s in cody2 if "청" in s) # 하의에 "청"이 있으면
             cody3 = list(set([s for s in cody2 if "청" in s])) # "청"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "회" in s) # 상의에 "회"이 있으면
             cody4 = list(set([s for s in cody1 if "회" in s])) # "회"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
         elif('17.0' >= a[13]):
             cody1 = list(set([s for s in L1 if "나시티" in s] + [s for s in L1 if "민소매" in s] + [s for s in L1 if "반" in s])) #상의 조건결과
             cody2 = list(set([s for s in L2 if "반" in s])) #하의 조건결과
             (s for s in cody2 if "청" in s) # 하의에 "청"이 있으면
             cody3 = list(set([s for s in cody2 if "청" in s])) # "청"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "회" in s) # 상의에 "회"이 있으면
             cody4 = list(set([s for s in cody1 if "회" in s])) # "회"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
             (s for s in cody2 if "검" in s) # 하의에 "검"이 있으면
             cody3 = list(set([s for s in cody2 if "검" in s])) # "검"들어간 옷들 다 넣는다(하의)
             (s for s in cody1 if "흰" in s) # 상의에 "흰"이 있으면
             cody4 = list(set([s for s in cody1 if "흰" in s])) # "흰"들어간 옷들 다 넣는다(상의)
             n1 = len(cody3) #하의 길이
             n2 = len(cody4) #상의 길이
             if(n1 > n2): #하의가 상의보다 같거나 많으면
                for i in cody3:
                    for j in cody4:
                        print(j + "+" + i)
                cody3 = list()
                cody4 = list()
             else:
                for i in cody4:
                    for j in cody3:
                        print(i + "+" + j)
                cody3 = list()
                cody4 = list()
