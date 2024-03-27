def random_number_gen(x0=1000, a=24693, c=3517, k=(2**17), precision=4):
      while True:
        x_i = (a * x0 + c) % k
        yield round(x_i/k, precision)
        x0 = x_i


if __name__ == "__main__":
    #Testing random number gen
    gen = random_number_gen()
    for i in range(1, 54):
        x = next(gen)
        if i in {51, 52, 53}:
            print(f"U_{i}="+str(x))

