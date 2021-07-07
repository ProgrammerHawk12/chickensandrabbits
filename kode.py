tnor = 0#temporary number of rabbits
tnoc = 0#temporary number of chickens
ctr = 0#counter to iterate through possibilities
c = False# to see whether the values of each variable have switched yet
for i in range(70):#loop for 70 times
    ctr += 1#adding one to our counter, to make a new possibility to test
    if ctr == 35:#sees if the counter is equal to thirty five, then restarting the counter for the chickens, rather than rabbits, by switching them for this iteration, and for the next iteration, by setting c to true
        ctr = 1
        tnor = 35 - ctr
        tnoc = ctr
        c = True
    if c:#seeing if c is true, if so, using the counter for the chickens, and setting the possibilities
        tnor = 35 - ctr
        tnoc = ctr
    else:#if c is not true, using the counter for the rabbits, and getting the possibilites
        tnor = ctr
        tnoc = 35 - ctr
    tnorl = tnor * 4#getting the number of rabbit legs for this possibility
    tnocl = tnoc * 2#getting the number of chicken legs for this possibility
    if tnorl + tnocl == 94:#checking if the possibility works, and stopping the loop if it does
        break
print(f'the number of rabbits is {tnor}, and the number of chickens is {tnoc}')#printing the final results