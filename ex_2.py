import random
#    generate_tuples(n, model):
# 1:    for i = 1 to n:
# 2:       v = empty array
# 3:       for V in model.variables:
# 4:          pa = v[V.Pa]    # parents of V
# 5:          v.append(sample(V.CPT(pa)))
# 6:       output v

def e_value():
    return 1 if random.random() < 1/111 else 0

def b_value():
    return 1 if random.random() < 0.00273972602 else 0

def a_value(e, b):
    if e == 1 and b == 1:
        return 1 if random.random() < 0.97 else 0
    if e == 1 and b == 0:
        return 1 if random.random() < 0.81 else 0
    if e == 0 and b == 1:
        return 1 if random.random() < 0.92 else 0
    if e == 0 and b == 0:
        return 1 if random.random() < 0.0095 else 0

          
def generate_tuples(n):
    v = []
    for _ in range(n):
        e = e_value()
        b = b_value()
        a = a_value(e, b)
        v.append([e, b, a])
    return v

n=100000
tuples = generate_tuples(n)
print("P(B|A)")
count1 = 0
for i in tuples:
    if i[1] == 1 and i[2] == 1:
        count1 += 1
count2 = 0
for i in tuples:
    if i[2] == 1:
        count2 += 1

# count1 /= n
# count2 /= n
print(count1/count2)

print("P(B|A, E)")
count1 = 0
for i in tuples:
    if i[1] == 1 and i[2] == 1 and i[0] == 1:
        count1 += 1
count2 = 0
for i in tuples:
    if i[2] == 1 and i[0] == 1:
        count2 += 1

# count1 /= n
# count2 /= n
print(count1/count2)

# def calculate_propability(tuples):
#     n = len(tuples)
#     correct_tuples = []
#     for i in tuples:
#         # if i[2] == 1:
#         #     if i[1] == 1:
#         #         correct_tuples.append("P(A|B)")
#         if i[1] == 1:
#             if i[2] == 1:
#                 correct_tuples.append("P(B|A)")
#         # if i[1] == 1:
#         #     if i[2] == 1:
#         #         if i[0] == 1:
#         #             correct_tuples.append("P(B|A, E)")
#         # if i[2] == 1 and i[0] == 1:
#         #     if i[1] == 1:
#         #         correct_tuples.append("P(A and E|B)")
    

#     return f"{correct_tuples[0]}:", len(correct_tuples)/n

# n=100000
# tuples = generate_tuples(n)
# print(calculate_propability(tuples))
