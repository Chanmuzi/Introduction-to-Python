# 일반적인 운송수단을 나타내는 클래스
class Vehicle:
    def __init__(self, make, model, color, price):
        self.make = make        # 메이커
        self.model = model      # 모델
        self.color = color      # 색상
        self.price = price      # 가격

    def setMake(self,make):     # 설정자 메소드
        self.make = make

    def getMake(self):          # 접근자 메소드
        return self.make

    # 차량에 대한 정보를 문자열로 요약하여 반환
    def getDesc(self):
        return '차량 =('+str(self.make)+','+\
                                            str(self.model)+','+\
                                            str(self.color)+','+\
                                            str(self.price)+')'
