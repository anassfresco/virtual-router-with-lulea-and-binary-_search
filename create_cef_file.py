from create_random_ips import router
import random
import re
import csv





def decimal_binary_for_tree(ip):
    binary_ip=""
    match = re.search(r'(\d+).(\d+).(\d+).(\d+)', ip)
    for i in range(1,5):
        to_bin=bin(int(match.group(i)))
        groupe=to_bin.replace("0b",((8-(len(to_bin)-2))*"0"))
        binary_ip+=groupe
    return binary_ip

##csv_file to add each ip with its binary value



with open("table_routage.csv","w",newline="") as new_file:
    filed_name=["network","mask","binary_network","mask_binary","interface"]
    csv_writter=csv.writer(new_file)
    csv_writter.writerow(filed_name)
    for i in router.fib:
        csv_writter.writerow([i.ip,i.mask,decimal_binary_for_tree(i.ip),decimal_binary_for_tree(i.mask),i.interface])

new_file.close()