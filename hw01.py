
filename = "hw0_data.dat";
fl = open(filename,"r");
ls = [];
mid = [];
positive = [];
negative = [];
result = [];
choice = input("please select a column to sort:");
if choice == 0:
    print("index error");
    exit();
try:
    for line in fl:
        ls = line.split(" ");
        mid.append(float(ls[choice-1]));
    for ele in mid:
        if ele > 0:
            positive.append(ele);
        else:
            negative.append(ele);
    negative.sort();
    positive.sort();
    result = negative + positive;
    print(result);
except IndexError:
    print("index error");
fl.close();
