class Customer():
    def __init__(self, cid=None, name=None, address=None, email =None, mobile = None):
        self.cid = cid
        self.name = name
        self.address = address
        self.email = email
        self.mobile = mobile

    # Getters
    def getCID(self):
        return self.cid
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getMobile(self):
        return self.mobile
    # Setters
    def setDID(self, cid):
        self.cid = cid
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setEmail(self, email):
        self.email = email
    def setMobile(self,mobile):
        self.mobile = mobile
    # str
    def __str__(self):
        return str(self.cid)+", "+self.name+", "+self.address+", "+self.email+", "+self.mobile