import re
import csv

class node:
    def __init__(self):
        self.data=None
        self.children=[None]*(2**4)
        self.bittar=[]
        self.vallar=[]
        self.interface=None




class lulia:
    def __init__(self):
        self.root=node()
        self.root.data="pointer"
        self.strid=4
        self.not_empty_children=[]





##Etape	1:	MulA-Bit	Trie:	fixed stride
    def insert(self,ip,mask,interfce):
        ip=self.decimal_binary_for_tree(ip)
        ip_with_strid=self.make_stride(ip,mask) ##devide ip by 4
        actual_node=self.root
        for i in ip_with_strid:
            if actual_node.children[int(i,2)] is None:
                actual_node.children[int(i,2)]=node()
            actual_node=actual_node.children[int(i,2)]
        actual_node.data="".join(ip_with_strid)
        actual_node.interface=interfce

    def make_stride(self,ip,mask):
        i=0
        new_ip=[]
        while i<mask:
            j=i
            str=""
            while j<i+4:
                str+=ip[j]
                j=j+1
            new_ip.append(str)
            i+=self.strid
        return new_ip


    def decimal_binary_for_tree(self,ip):
        binary_ip = ""
        match = re.search(r'(\d+).(\d+).(\d+).(\d+)', ip)
        for i in range(1, 5):
            to_bin = bin(int(match.group(i)))
            groupe = to_bin.replace("0b", ((8 - (len(to_bin) - 2)) * "0"))
            binary_ip += groupe
        return binary_ip




##Etape	2:	leaf pushing
    def get_leaf(self):
        actual_node=self.root
        liste=[actual_node]

        not_empty_node=[]
        not_empty_children=[]

        while len(liste)!=0:
            for i in liste[0].children:
                if i is None:
                    continue
                
                if i.children!=[None]*(2**self.strid):
                    liste.append(i)
                    not_empty_children.append(i)
                if (i.data is not None) and  i.children!=[None]*(2**self.strid):
                    not_empty_node.append(i)
            del liste[0]
        self.not_empty_children=not_empty_children
        return not_empty_node
    def leaf_pushing(self):
        leaf=self.get_leaf()
        for i in leaf:
            j=0
            while j<len(i.children):
                if i.children[j] is None:
                    i.children[j]=node()
                    i.children[j].data = i.data
                j=j+1
            i.data="pointer{}".format(i.data)





#Etape	3:éliminer les	éléments	redondants

    def final(self):
        liste=[self.root]+self.not_empty_children
        for i in liste:
            i.bittar=self.bittar(i)
            i.vallar=self.vallar(i)


    def bittar(self,node):
        bitarr = [1]+[None]*((2**(self.strid))-1)
        i=0
        while i<len(node.children)-1:
            if node.children[i]!=node.children[i+1]:
                bitarr[i+1]=1
            else:
                bitarr[i+1]=0
            if node.children[i]==None and node.children[i+1]==None:
                bitarr[i + 1] = 1
            i=i+1
        return bitarr






    def vallar(self,node):
        i=0
        vallar=[]
        while i<len(node.children):
            j=i
            while j<len(node.children)-1 and  node.children[i]==node.children[j+1] and node.children[i]!=None:
                j=j+1
            vallar.append(node.children[i])
            i=j+1
        return vallar



####loockup

    def lockup(self,ip):
        mask=self.get_mask(ip)
        ip=self.decimal_binary_for_tree(ip)
        new_ip=self.make_stride(ip,mask)
        actual_node=self.root
        for i in new_ip:
            print(i)

            index=int(i,2)
            true_index=self.get_index(actual_node.bittar,index)
            actual_node=actual_node.vallar[true_index]
        return actual_node.interface







    def get_index(self,liste,index):
        k=0
        get_index=0
        while k<index:
            if liste[k]==1:
                get_index+=1
            k=k+1
        return k









    def get_mask(self, ip):
        match = re.search(r'(\d+).(\d+).(\d+).(\d+)', ip)
        ip = match.group(1)
        mask = 0
        if 0 <= int(ip) <= 127:
            mask = 8

        elif 128 <= int(ip) < 192:
            mask = 16
        elif 192 <= int(ip) < 224:

            mask = 24
        return mask


lulia1=lulia()



with open("table_routage.csv","r") as f:
    read_file=csv.reader(f)
    delimeter=next(read_file)
    for i in read_file:
        try:
            ip = i[0]

            pattern = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).(\d{1,2})', ip)
            mask = int(pattern.group(2))
            ip1 = pattern.group(1)
            interface = i[4]
            lulia1.insert(ip1, mask, interface)
        except:
            pass

lulia1.leaf_pushing()
lulia1.final()




