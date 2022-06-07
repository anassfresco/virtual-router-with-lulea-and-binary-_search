import random
class network:
    def __init__(self,ip,mask,interface):
        self.ip=ip
        self.mask=mask
        self.interface=interface

class cef:
    def __init__(self):
        self.fib=[]

    def ip(self,a,b):
        ip=str(random.randrange(a,b))
        for i in range(3):
            ip+="."+str(random.randrange(255))
        return ip
    def random_network(self):

        for i in range(500):
            if i <= 200:
                ip_c = self.ip(192, 224)+"/24"
                interface="ethernet"+str(random.randint(1,50))
                node=network(ip_c,"255.255.255.0",interface)
                self.fib.append(node)
            if i <= 300:
                ip_b = self.ip(128, 192)+"/16"
                interface = "ethernet" + str(random.randint(1, 50))
                node = network(ip_b, "255.255.0.0", interface)
                self.fib.append(node)
            ip_a = self.ip(0, 127)+"/8"
            interface = "ethernet" + str(random.randint(1, 50))
            node = network(ip_a, "255.0.0.0", interface)

            self.fib.append(node)
router=cef()
router.random_network()
random.shuffle(router.fib)




