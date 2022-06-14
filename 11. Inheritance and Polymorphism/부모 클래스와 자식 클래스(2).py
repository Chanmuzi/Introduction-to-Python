class Truck(Vehicle):
    def __init__(self,make,model,color,price,payload):
        super().__init__(make,model,color,price)
        self.payload=payload

    def setPayload(self,payload):   # 설정자 메소드
        self.payload=payload

    def getPayload(self):           # 접근자 메소드
        return self.payload
