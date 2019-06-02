from naverWeather import *
from room import *
from erumyFortune import *

while(1):
 print("\n<<<<<<<<<<<<<<<<<<<<<<<메뉴를 선택하세요.>>>>>>>>>>>>>>>>>>>>>>>")
 print("1번 : 검색 | 2번 : 옷장 | 3번 : 옷장으로 코디해주기 | 4번 : 종료")
 control = input()
 if control == '1': # 1번 입력 시
  print("지역명을 입력해주세요.")
  area=input()
  if area in naverWeather.map_cityNum: # 올바른 도시명 입력 시
   print(naverWeather(area).getWeather())
   erumyFortune.fortune_5()
  elif area =='': # 공백 입력 시
   print(naverWeather("서울").getWeather())
   erumyFortune.fortune_5()
  else: # 잘못된 도시명 입력 시
   while(area not in naverWeather.map_cityNum):
    print("잘못된 도시명입니다. 다시 입력하세요")
    area=input()
    if area in naverWeather.map_cityNum:
      print(naverWeather(area).getWeather())
      erumyFortune.fortune_5()
    elif area =='': # 공백 입력 시
      print(naverWeather("서울").getWeather())
      erumyFortune.fortune_5()

 elif control == '2': # 2번 입력 시
  while(1):
      print("-------------------------------------------------")
      print("                <<< 옷     장 >>>                ")
      print("1번 : 상의 | 2번 : 하의 | 3번 : 종료")
      print("-------------------------------------------------")
      roomnum = input()
      if roomnum == '1':
          room.room_1()
      elif roomnum == '2':
          room.room_2()
      elif roomnum == '3':
          break
      else:
          print("<<<<<<잘못입력하셨습니다. 다시입력해주세요>>>>>>")
          print("")
 elif control == '3': # 3번 입력 시
  print("지역명을 입력해주세요.")
  area=input()
  if area in naverWeather.map_cityNum: # 올바른 도시명 입력 시
   print(naverWeather(area).getWeather())
   room.support(area)
  elif area =='': # 공백 입력 시
   print(naverWeather("서울").getWeather())
  else: # 잘못된 도시명 입력 시
   while(area not in naverWeather.map_cityNum):
    print("잘못된 도시명입니다. 다시 입력하세요")
    area=input()
    if area in naverWeather.map_cityNum:
      print(naverWeather(area).getWeather())
 elif control == '4': # 4번 입력 시
  print("프로그램을 종료합니다.")
  break
 else:
     print("다시입력해주세요")
