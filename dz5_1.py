def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num
max_gen_15 = nums_generator(15)
for i in max_gen_15:
    print(i)