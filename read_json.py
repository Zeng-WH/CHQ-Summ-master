import json
import numpy as np
import math

def main():
    with open('/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum/train.json', 'r') as r:
        a = json.load(r)
    random_seed = np.arange(len(a))
    np.random.shuffle(random_seed)
    train_seed = random_seed[0: math.floor(0.8*len(random_seed))]
    dev_seed = random_seed[math.floor(0.8*len(random_seed)) : ]
    train_list = []
    for item in train_seed:
        train_list.append(a[item])
    dev_list = []
    for item in dev_seed:
        dev_list.append(a[item])

    with open("/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum_split/train.json", "w") as w:
        json.dump(train_list, w)
    with open("/home/disk1/dgt2021/zwh/CHQ-Summ-master/dataset/meqsum_split/dev.json", "w") as w:
        json.dump(dev_list, w)


    print("bupt")


if __name__ == '__main__':
    main()