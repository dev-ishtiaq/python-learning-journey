# def my_gen():
#     yield 1
#     yield 2
#     yield 3

# for value in my_gen():
#     print(value)

# -count -------
# def count_num(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# for num in count_num(10):
#     print(num)            

# def myGen():
#     for i in range(100):
#         yield i

# gen = myGen()   

# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# for j in gen:
#     print(j)


# def continuous_gen():
#     i = 0
#     while i <= 10:
#         sq = i*i
#         yield sq
#         i += 1

# value = continuous_gen()
# for v in value:
#     print(v)

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# gen = fibonacci()
# for _ in range(100):
#     print(next(gen)


# ------send() Method----
# def generator_with_send():
#     while True:
#         received = yield
#         print("Received:", received)

# gen = generator_with_send()
# next(gen)
# gen.send("Hello")
# gen.send("Dear")        


# --close() Method----
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed.")

gen = my_gen()
print(next(gen))
print(next(gen))
gen.close()  # This will trigger the finally block