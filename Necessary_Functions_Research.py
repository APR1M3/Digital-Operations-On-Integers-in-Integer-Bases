import matplotlib.pyplot as plt
import numpy as np


# Mild use of Claude to error check certain modules
# Use of Rosetta Code's module for conversion to negative bases
# https://rosettacode.org/wiki/Negative_base_numbers#Python

def EncodeNegBase(num, base):  # Converts from decimal
    if num == 0:
        return "0"
    out = []
    while num != 0:
        num, rem = divmod(num, base)
        if rem < 0:
            num += 1
            rem -= base
        out.append(rem)
    return "".join(map(str, out[::-1]))


# print(EncodeNegBase(146, -3))
# Outputs 21102


# Sum of digits of a number using divmod
def digitsum(num, base):
    total = 0
    if num < 0:
        num *= (-1)

        if base < 0:
            converted = EncodeNegBase(num, base)
            length = len(converted)
            for i in range(length):
                total += int(converted[i])
        else:
            while num != 0:
                checktuple = divmod(num, base)
                digit = (-1) * checktuple[1]
                total += digit
                num = checktuple[0]

    else:
        if base < 0:
            converted = EncodeNegBase(num, base)
            length = len(converted)
            for i in range(length):
                total += int(converted[i])
        else:
            while num != 0:
                checktuple = divmod(num, base)
                digit = checktuple[1]
                total += digit
                num = checktuple[0]

    return total


# print(digitsum(-15, 10))
# Outputs -6

# Product of digits of a number using divmod
def digitprod(num, base):
    product = 1
    if num < 0:
        num *= (-1)

        if base < 0:
            converted = EncodeNegBase(num, base)
            length = len(converted)
            for i in range(length):
                product *= int(converted[i])
        else:
            while num != 0:
                checktuple = divmod(num, base)
                digit = (-1) * checktuple[1]
                product *= digit
                num = checktuple[0]

    else:
        if base < 0:
            converted = EncodeNegBase(num, base)
            length = len(converted)
            for i in range(length):
                product *= int(converted[i])
        else:
            while num != 0:
                checktuple = divmod(num, base)
                digit = checktuple[1]
                product *= digit
                num = checktuple[0]

    return product


# print(digitprod(15, -10))
# Outputs 45 (195)

# print(digitsum(-15,-10))
# Outputs 15 (195)

# print(digitprod(-15, 10))
# Outputs 5

def sumplusprod(num, base):
    value = digitsum(num, base) + digitprod(num, base)
    return value


def summinusprod(num, base):
    value = digitsum(num, base) - digitprod(num, base)
    return value


def sumtimesprod(num, base):
    value = digitsum(num, base) * digitprod(num, base)
    return value


def sumoverprod(num, base):
    if digitprod(num, base) > 0:
        value = digitsum(num, base) / digitprod(num, base)
        return value
    else:
        return 0


def repeatplus(num, base):
    value = num
    valuelist = [value]
    print(value)
    value = sumplusprod(value, base)
    while value not in valuelist:
        valuelist.append(value)
        print(value)
        value = sumplusprod(value, base)

    length = len(valuelist)
    for i in range(length):
        if valuelist[i] == value:
            looplength = length - i
            print("")
            print(f"Length of loop is {looplength} value(s)")
            print(f"{value} is a {looplength}-periodic S+P number")

    return looplength

def repeatminus(num, base):
    value = num
    valuelist = [value]
    print(value)
    value = summinusprod(value, base)
    while value not in valuelist:
        valuelist.append(value)
        print(value)
        value = summinusprod(value, base)

    seqlength=len(valuelist)
    return seqlength 


def repeattimes(num, base):
    value = num
    valuelist = [value]
    print(value)
    value = sumtimesprod(value, base)
    while value not in valuelist:
        valuelist.append(value)
        print(value)
        value = sumtimesprod(value, base)

    length = len(valuelist)
    for i in range(length):
        if valuelist[i] == value:
            looplength = length - i
            print("")
            print(f"Length of loop is {looplength} value(s)")
            print(f"{value} is a {looplength}-periodic S.P number")

    return looplength

def repeatdivide(num, base):
    value = num
    valuelist = [value]
    print(value)
    value = sumoverprod(value, base)
    while value not in valuelist and value >=1 and int(value)=value:
        valuelist.append(value)
        print(value)
        value = sumoverprod(value, base)
        
    seqlength=len(valuelist)
    return seqlength

# repeattimes(128,7)
# Outputs "Length of loop is 1 value(s)"

# print("")

# repeatplus(12,-7)
# Outputs "Length of loop is 7 value(s)"

def sumplusprodcheck(uplim, base, tasknum):
    if tasknum == 1:
        xlist = []
        ylist = []
        for i in range(1, uplim + 1):
            xlist.append(i)
            ylist.append(sumplusprod(i, base))
            totaladd += sumplusprod(i, base)

        averageadd = totaladd / uplim

        plt.figure(figsize=(20, 10))
        plt.plot(xlist, ylist)
        plt.hlines(y=[averageadd], xmin=1, xmax=uplim, colors=['g'], linestyles=[':'])
        plt.xlabel("Integers Up To A Certain Limit")
        plt.ylabel("Total of Digit Sum and Digit Product")
        plt.title("S+P graph")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    elif tasknum == 2:
        for i in range(1, uplim + 1):
            totaladd = 0
            add = sumplusprod(i, base)
            totaladd += add
            print(f"{i} has an S+P value of {add}")

        averageadd = totaladd / uplim
        print(f"{averageadd} is the average S+P value")

    elif tasknum == 3:

        for i in range(1, uplim + 1):
            add = sumplusprod(i, base)
            if add == i:
                print(i)

    elif tasknum == 4:

        for i in range(1, uplim + 1):
            add = sumplusprod(i, base)
            if add < i:
                print(i)

    elif tasknum == 5:

        for i in range(1, uplim + 1):
            add = sumplusprod(i, base)
            if add > i:
                print(i)

    else:
        print("Please input a valid task number")


# sumplusprodcheck(1000,10,1)
# Produces graph of S+P with baseline as average value

# sumplusprodcheck(1000, 10, 2)
# Outputs S+P for all numbers in range, then outputs average S+P

# sumplusprodcheck(1000000, 10,3)
# Outputs 19,29, ..., 99 (S+P numbers) within a certain range (1 to upper bound)

# sumplusprodcheck(1000, 10, 4)
# Outputs all sub-S+P numbers within said certain range

# sumplusprodcheck(1000, 10, 5)
# Outputs all super-S+P numbers within said certain range

def sumtimesprodcheck(uplim, base, tasknum):
    if tasknum == 1:
        xlist = []
        ylist = []
        for i in range(1, uplim + 1):
            xlist.append(i)
            ylist.append(sumtimesprod(i, base))
            totalprod += sumtimesprod(i, base)

        averageprod = totalprod / uplim

        plt.figure(figsize=(20, 10))
        plt.plot(xlist, ylist)
        plt.hlines(y=[averageprod], xmin=1, xmax=uplim, colors=['g'], linestyles=[':'])
        plt.xlabel("Integers Up To A Certain Limit")
        plt.ylabel("Product of Digit Sum and Digit Product")
        plt.title("S.P graph")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    elif tasknum == 2:
        for i in range(1, uplim + 1):
            totalprod = 0
            prod = sumtimesprod(i, base)
            totalprod += prod
            print(f"{i} has an S.P value of {prod}")

        averageprod = totalprod / uplim
        print(f"{averageprod} is the average S+P value")

    elif tasknum == 3:

        for i in range(1, uplim + 1):
            prod = sumtimesprod(i, base)
            if prod == i:
                print(i)

    elif tasknum == 4:

        for i in range(1, uplim + 1):
            prod = sumtimesprod(i, base)
            if prod < i:
                print(i)

    elif tasknum == 5:

        for i in range(1, uplim + 1):
            prod = sumtimesprod(i, base)
            if prod > i:
                print(i)

    else:
        print("Please input a valid task number")


# sumtimesprodcheck(1000,10,1)
# Produces graph of S.P with baseline as average value

# sumtimesprodcheck(1000, 10, 2)
# Outputs S.P for all numbers in range, then outputs average S.P

# sumtimesprodcheck(1000000, 10,3)
# Outputs  1, 135, 144 (S.P numbers) within a certain range (1 to upper bound)

# sumtimesprodcheck(1000, 10, 4)
# Outputs all sub-S.P numbers within said certain range

# sumplusprodcheck(1000, 10, 5)
# Outputs all super-S.P numbers within said certain range


def spratiocheck(uplim, base, tasknum):
    if tasknum == 1:
        ratiolist = []
        indexlist = []
        totalratio = 0
        for i in range(1, uplim + 1):
            indexlist.append(i)
            ratiolist.append(sumoverprod(i, base))
            totalratio += sumoverprod(i, base)

        averageratio = totalratio / uplim

        plt.figure(figsize=(20, 10))
        plt.plot(indexlist, ratiolist)
        plt.hlines(y=[averageratio], xmin=1, xmax=uplim, colors=['g'], linestyles=[':'])
        plt.xlabel("Integers Up To A Certain Limit")
        plt.ylabel("Ratio of Digit Sum to Digit Product")
        plt.title("S:P ratio graph")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    elif tasknum == 2:
        totalratio = 0
        for i in range(1, uplim + 1):
            ratio = sumoverprod(i, base)
            print(f"{i} has an S:P ratio of {ratio}")
            totalratio += ratio

        averageratio = totalratio / uplim

        print(f"{averageratio} is the average ratio")

    elif tasknum == 3:
        for i in range(1, uplim + 1):
            ratio = sumoverprod(i, base)
            if ratio == 1:
                print(i)

    elif tasknum == 4:
        for i in range(1, uplim + 1):
            ratio = sumoverprod(i, base)
            if ratio < 1:
                print(i)

    elif tasknum == 5:
        for i in range(1, uplim + 1):
            ratio = sumoverprod(i, base)
            if ratio > 1:
                print(i)


    else:
        print("Please enter a valid task number")

# spratiocheck(1000,10,1)
# Produces graph of S:P with baseline as average ratio

# spratiocheck(1000, 10, 2)
# Outputs ratios for all numbers in range where product is not 0, then outputs average ratio

# spratiocheck(1000000, 10,3)
# Outputs 1,2,..., 123,132, ... (S:P numbers) within a certain range (1 to upper bound)

# spratiocheck(1000, 10, 4)
# Outputs all sub-S:P numbers within said certain range

# spratiocheck(1000, 10, 5)
# Outputs all super-S:P numbers within said certain range





