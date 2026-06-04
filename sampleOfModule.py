'''
import myModule as mm

print(mm.myListOfFruits)
print(mm.tupleOfFlowers)

mm.sample()

'''
from myAnotherModule import sample as sample1
from myModule import sample as sample2


sample1()
sample2()
