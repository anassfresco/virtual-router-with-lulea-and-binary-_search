import re
import csv

class node:
    def __init__(self,data):
        self.data=data
        self.right_child=None
        self.left_child=None
        self.interface=None

class binary:
    def __init__(self):
        self.root=node("pointer")
    def insert_ip(self,ip,mask,interface):
        ip=self.decimal_binary_for_tree(ip)
        actual_node=self.root
        for i in range(0,mask):
            if ip[i]=="0":
                if actual_node.left_child is None:
                    actual_node.left_child=node(ip[i])
                actual_node=actual_node.left_child
            else:
                if actual_node.right_child is None:
                    actual_node.right_child=node(ip[i])
                actual_node=actual_node.right_child

        actual_node.interface=interface
    def loockup(self,ip):

        mask=self.get_mask(ip)
        binary_ip=self.decimal_binary_for_tree(ip)

        return self.loockup_ip(binary_ip,mask)

    def get_mask(self,ip):
        match = re.search(r'(\d+).(\d+).(\d+).(\d+)', ip)
        ip=match.group(1)
        mask=0
        if  0<=int(ip)<=127:
            mask=8

        elif 128<=int(ip)<192:
            mask=16
        elif 192<=int(ip)<224:

            mask=24
        return mask


    def loockup_ip(self,ip,mask):
        actual_node=self.root
        for i in ip[0:mask]:
            print(i)
            if i == "0":
                actual_node = actual_node.left_child

            else:
                actual_node = actual_node.right_child
        return "output_interface_is :"+actual_node.interface

    def decimal_binary_for_tree(self,ip):
        binary_ip = ""
        match = re.search(r'(\d+).(\d+).(\d+).(\d+)', ip)
        for i in range(1, 5):
            to_bin = bin(int(match.group(i)))
            groupe = to_bin.replace("0b", ((8 - (len(to_bin) - 2)) * "0"))
            binary_ip += groupe
        return binary_ip



binary1=binary()

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
            binary1.insert_ip(ip1, mask, interface)
        except :
            pass
f.close()








