import json

with open("/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum_split/train.json", "r") as w:
    a = json.load(w)
with open("/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum_split/dev.json", "r") as w:
    b = json.load(w)

a =  a[:20]
b = b [:5]
with open("/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum_small/train.json", "w") as w:
    json.dump(a, w)
with open("/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum_small/dev.json", "w") as w:
    json.dump(b, w)

print("bupt")
