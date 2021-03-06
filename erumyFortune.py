import requests
import datetime
from bs4 import BeautifulSoup
from datetime import datetime

APIUrl = 'http://www.erumy.com/free/todayFortuneReport.aspx'

class erumyFortune:

    def fortune_1(self): # 입력받은 수로 랜덤수 만들기
        now = datetime.now()
        a = (int(now.second) + int(now.minute) - self - 20000000)
        return a

    def make_dict(self, soup):
        tmpres = str(soup.select('label > ul')[0])
        today_fortune = tmpres[4:-5]
        tmpres = soup.select('div > font > label')[0]
        today = tmpres.get_text('label')
        return {'Fortune': today_fortune, 'day': today}

    def today_tell(self, birth):
        func_url = APIUrl + '?m=dummy&uday=' + birth + '&lunar=1'
        r = requests.get(func_url, auth=('user', 'pass'))
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        return self.make_dict(soup)

    def fortune_2(self): # 랜덤수 나머지 구하기
        a = self % 10
        return a

    def tomorrow_tell(self, birth):
        now = datetime.date.today()
        now = now + datetime.timedelta(days=1)
        tomorrow = '{0:02d}{1:02d}{2:02d}'.format(now.year, now.month, now.day)
        func_url = APIUrl + '?m=dummy&uday=' + birth + '&lunar=1' + '&NextDay=T&tday=' + tomorrow
        r = requests.get(func_url, auth=('user', 'pass'))
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        return self.make_dict(soup)
        
    def fortune_3(self): # 운세정리
        if(self == 0):
            print("오늘은 누군가로부터 큰 도움을 받을 것 같은 막연한 기대심리가 우러나며, 실제로 약간 부담스러운 도움을 받을 가능성도 많은 편입니다. 연장자나 상사와의 유대관계에서 도움을 받는 일이 생기기 쉬우며, 관공서와 공공기업으로부터 문서상의 권익을 얻을 수 있습니다. 또한 각종 법적인 문서상의 권리(주택, 부동산, 자격증, 특허 등)를 취득하거나, 신문 또는 방송에 나오거나, 표창을 수여하는 등 명예스러운 증서를 받을 수 있는 운입니다. 병무, 경찰, 검찰 등에서 발부하는 문서를 접수하게 되거나 연락해야 할 일이 생기기 쉬운 날입니다.")
        elif(self == 1):
            print("오늘은 기운이 나면서 협동심이 생기는 날입니다. 부모의 좋은 배경과 학식을 겸비한 사람을 만나게 될 것인데, 보수적이며 고전적인 인격을 서로 이해하고 존중하면 아주 좋은 관계로 발전하여 특정재산의 공동관리 또는 연구 등의 분야에서 성공과 발전이 가능하지만, 자존심을 내세우며 대립하면 서로에게 상처만 줄 뿐 아무 결실도 맺지 못하게 됩니다. 서로의 개성을 진심으로 존중하고 이해하려는 노력이 필요한 날입니다.")
        elif(self == 2):
            print("오늘은 마음이 안정되고 모든 소망이 성취될 것 같은 느낌이 듭니다. 취직, 인허가, 은행 융자와 같은 공공기관을 대상으로 하는 일에서 타인의 도움을 받게 될 것입니다. 정치와 국가 문제까지도 관심을 갖게 되며, 공금과 국가예산, 공적인 자금의 융통과 신용문제를 의논하게 됩니다. 모든 사람이 호감을 갖고 대해 줄 것이므로 일이 쉽게 해결될 수 있는 날입니다. 그러나 자신이 원하는 것을 얻기 위해서 또는 명예를 지키기 위해 많은 지출을 해야 할 가능성도 있습니다. 때로는 명예를 얻거나 더 좋은 직장을 구하기 위해 투자와 노력을 하는 경우가 생기기도 합니다.")
        elif(self == 3):
            print("오늘은 만사가 형통할 것 같은 느낌이 듭니다. 생각하고 행동하는 것이 한치의 오차도 없이 이루어질 수 있으므로, 돈도 생기고 원하던 것도 생기는 행운의 날입니다. 특히 학문적 또는 교육적인 문제가 운세와 연결되어 뜻대로 성취되기 쉽습니다. 경제적인 안정이나 생활의 풍요로움을 원하는 경우에는 이를 이룰 수 있는 계기를 마련하게 될 것입니다. 그러나 노력한 만큼의 성과만을 기대해야 할 날입니다. 금전의 활용과 이익창출에 대한 새로운 지식을 얻거나 활로를 모색하게 할 수 있습니다.")
        elif(self == 4):
            print("오늘은 뜻밖의 횡재가 생길 것 같은 느낌이 듭니다. 혹시 돼지꿈을 꾸지 않으셨습니까? 무심코 한 말이나 생각이 정확하게 들어 맞아 횡재수가 생길 수 있는 날이므로 증권, 복권, 경마 등에 관심을 가지게 될 가능성이 큽니다. 허황된 생각이 의외로 들어맞을 가능성이 많은 편이지만, 이러한 일에 너무 기대를 가져서는 안됩니다. 언어와 화술로써 큰 돈을 쉽게 벌고자 하는 생각이 적중되며 불로소득의 욕망을 충족할 수 있습니다.")
        elif(self == 5):
            print("오늘은 남들이 자신을 도와줄 것 같은 막연한 기대가 생기거나 자만은 하게 될 가능성이 많은 반면, 예감이 정확하게 적중하는 경우도 생기기 쉬울 것입니다. 다른 사람을 위해 중간 역할을 하는 것을 보람으로 생각하며 자신의 실리보다도 남의 이익을 위해 노력하기도 합니다. 교육이나 학습에 관한 문제와 인연이 생기며 중간 역할로 남의 이익을 도모하는데 참여할 수도 있습니다. 실수를 범하거나 거만하게 보이기 쉬우니, 배우는 자세로 겸손하게 행동해야 손해를 보는 일이 생기지 않은 것입니다.")
        elif(self == 6):
            print("작은 일 하나로 크게 기뻐하게 되면서 새로운 힘을 얻을 수 있는 날이 될 것으로 보입니다. 너무 큰 기대나 무리한 일은 당신으로 하여금 실망을 안겨줄 수 있습니다. 그렇기 때문에 작은 것에도 만족할 수 있는 당신의 모습이 어느 때보다 큰 능력을 발휘할 것입니다. 주변의 모든 상황을 깨끗이 정리해 줄 수 있으며 당신이 가는 곳에 곧 당신의 목표와 연결되어 있다는 것을 기억하세요. 또한 당신의 능력에 대한 확신을 갖고 많은 체력이 필요한 일에 도전해 보면 좋은 성과가 있을 것이니 어서 밖으로 나가 보도록 하십시오.")
        elif(self == 7):
            print("기다렸던 약속이 이뤄지는 날이네요. 기대했던 곳에서 역시 좋은 결과를 볼 수 있고, 예상보다 빠른 성과에 당신도 놀라게 됩니다. 오랫동안 보고 싶었던 사람을 만나게 되거나 자신이 평소에 바래왔던 일이 기적처럼 일어나는 경우도 있습니다. 또한 가족에게 자랑할만한 사건이 생기는 날입니다. 친구에게서 좋은 소식을 들을 수도 있겠군요. 그만큼 자신도 노력을 아끼지 말아야 하며 일이 잘 풀릴 수록 자신에 대한 자만은 줄이고 낮추는 것이 오히려 더욱 좋은 운을 함께 할 수 있게 합니다.")
        elif(self == 8):
            print("솔직한 대화가 당신에게 큰 힘이 되는 날입니다. 행운이 가득하니 용기를 내세요. 적을 동지로 돌릴 수 있는 날입니다. 평소에 알고 지내던 사이에 작은 갈등이나 오해가 있었다면 자신이 먼저 마음을 열고 다가가는 것도 좋으며 혹은 상대방쪽에서 자신에게 손을 내미는 일이 생길 수 있습니다. 당신을 있는 그대로 솔직하게 표현하십시오. 또한 작은 일에 연연하기보다는 큰 흐름에 집중하는 것이 좋겠군요. 사소한 일보다는 큰 일에 신경을 쓰면서 일을 해나가세요. 자신감을 가지고 움직이면 그만큼 힘이 납니다.")
        elif(self == 9):
            print("일의 초반이 어려우나 뒤로 갈수록 전개가 빨라지고 해결이 쉽습니다. 한결같은 태도를 유지하세요. 일관되게 노력하면 많은 것을 해냅니다. 자신이 세운 목표를 중심으로 자신의 뜻을 이루도록 노력해보세요. 자신의 노력만큼 값진 행동은 없습니다. 또한 가족의 인정과 격려를 얻게 됩니다. 자신의 목표에 부합되는 만큼 멋진 성과를 기대하는 것도 나쁘지 않습니다. 초반에는 스트레스를 받을 수 있으나 점차 운세의 흐름이 당신에게 행운으로 돌아가고 있으니 자신감을 가지세요.")
        else:
            print("오늘은 누군가로부터 큰 도움을 받을 것 같은 막연한 기대심리가 우러나며, 실제로 약간 부담스러운 도움을 받을 가능성도 많은 편입니다. 연장자나 상사와의 유대관계에서 도움을 받는 일이 생기기 쉬우며, 관공서와 공공기업으로부터 문서상의 권익을 얻을 수 있습니다. 또한 각종 법적인 문서상의 권리(주택, 부동산, 자격증, 특허 등)를 취득하거나, 신문 또는 방송에 나오거나, 표창을 수여하는 등 명예스러운 증서를 받을 수 있는 운입니다. 병무, 경찰, 검찰 등에서 발부하는 문서를 접수하게 되거나 연락해야 할 일이 생기기 쉬운 날입니다.")

    def fortune_4(self): # submain함수
        a = self
        b = erumyFortune.fortune_1(a)
        c = erumyFortune.fortune_2(b)
        erumyFortune.fortune_3(c)

    def fortune_5():
        while(1):
            print("1번 : 오늘운세 확인 | 2번 : 종료")
            check = int(input())
            if check == 1:
                print("생년월일을 띄어쓰기 하지 마시고 적어주세요")
                date = int(input())
                erumyFortune.fortune_4(date)
            elif check == 2:
                break
            else:
                print("잘못입력하셨습니다. 다시입력해주세요\n")

    def someday_tell(self, birth, inputday):
        func_url = APIUrl + '?m=dummy&uday=' + birth + '&lunar=1' + '&NextDay=T&tday=' + inputday
        r = requests.get(func_url, auth=('user', 'pass'))
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        return self.make_dict(soup)
