from math import log
#calculate the outcomes for t<25 and t>25
CALL_OUTCOMES = {("LINE BUSY", 0.2, 9), ("UNAVAILABLE", 0.3, 31), ("AVAILABLE X<=25", 0.437743, 7), ("AVAILABLE X>25", 0.062258, 31)}

def random_number_gen(x0=1000, a=24693, c=3517, k=(2**17), precision=4):
    while True:
        x_i = (a * x0 + c) % k
        yield round(x_i/k, precision)
        x0 = x_i

def cont_rand_var_gen(random_num):
    return -12*log(1-random_num)

def discrete_rand_var_gen(random_num):
    final_outcome = (None, 1.0, None)
    for outcome in CALL_OUTCOMES:
        if (outcome[1] >= random_num and <= final_outcome):
            pass
            #still cooking


if __name__ == "__main__":
    #Testing random number gen
    gen = random_number_gen()
    for i in range(1, 54):
        x = next(gen)
        if i in {51, 52, 53}:
            print(f"U_{i}="+str(x))
    #Testing continuous rand var gen
    print(cont_rand_var_gen(0.8))

