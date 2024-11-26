import random
#    generate_tuples(n, model):
# 1:    for i = 1 to n:
# 2:       v = empty array
# 3:       for V in model.variables:
# 4:          pa = v[V.Pa]    # parents of V
# 5:          v.append(sample(V.CPT(pa)))
# 6:       output v

def b_value():
    return 1 if random.random() < 0.9 else 0

def r_value(b):
    if b == 0:
        return 0
    else:
        if random.random() < 0.1:
            return 0
        else:
            return 1

def i_value(b):
    if b == 0:
        return 0
    else:
        if random.random() < 0.05:
            return 0
        else:
            return 1
        
def g_value():
    return 1 if random.random() < 0.95 else 0
    
def s_value(i, g):
    if i == 0 or g == 0:
        return 0
    else:
        if random.random() < 0.01:
            return 0
        else:
            return 1

def m_value(s):
    if s == 0:
        return 0
    else:
        if random.random() < 0.01:
            return 0
        else:
            return 1
          
def generate_tuples(n):
    v = []
    for _ in range(n):
        b = b_value()
        r = r_value(b)
        i = i_value(b)
        g = g_value()
        s = s_value(i, g)
        m = m_value(s)
        v.append([b, r, i, g, s, m])
    return v

def calculate_propability(tuples):
    n = len(tuples)
    correct_tuples = []
    for i in tuples:
        # if i[0] == 1:
        #     if i[1] == 1:
        #         if i[3] == 1:
        #             if i[4] == 0:
        #                 correct_tuples.append("P(B|R,G,-S)")
        # if i[4] == 1:
        #     if i[1] == 1:
        #         if i[2] == 1:
        #             if i[3] == 1:
        #                 correct_tuples.append("P(S|R,I,G)")
        if i[0] == 1:
            if i[1] == 0:
                if i[2] == 1:
                    if i[3] == 1:
                        correct_tuples.append("P(B|-R,I,G)")
    

    return f"{correct_tuples[0]}:", len(correct_tuples)/n

n=100000
tuples = generate_tuples(n)
print(calculate_propability(tuples))
# "P(B|-R,I,G)" oli samaa, muut eri