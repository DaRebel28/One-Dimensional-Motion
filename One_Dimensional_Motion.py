# John Burghardt
from math import sqrt
m = None
a = None
t = None
x = None
V_i = None
V_f = None
unknowns = 0
while True :
    print("\033[H\033[2J",end="")
    print("One Dimensional Motion Calculator")
    print(" V_i     t      ∆x      a     V_f")
    print("m·-----------------------------→·")
    if isinstance(V_i, float) and isinstance(V_f, float) and V_f == V_i :
        a = 0
    if a == 0 :
        if isinstance(V_i, float) :
            V_f = V_i
        elif isinstance(V_f, float) :
            V_i = V_f
        if isinstance(t, float) and isinstance(x, float) and not isinstance(V_i, float) :
            V_i = x / t
            continue
        elif isinstance(t, float) and isinstance(V_i, float) :
            x = V_i * t
        elif isinstance(x, float) and isinstance(V_i, float) :
            t = x / V_i
    else :
        #V_f = V_i + at
        if isinstance(V_i, float) and isinstance(a, float) and isinstance(t, float) :
            V_f = V_i + a * t
        elif isinstance(V_f, float) and isinstance(a, float) and isinstance(t, float) :
            V_i = V_f - a * t
        elif isinstance(V_f, float) and isinstance(V_i, float) and isinstance(t, float) :
            a = (V_f - V_i) / t
        elif isinstance(V_f, float) and isinstance(V_i, float) and isinstance(a, float) :
            t = (V_f - V_i) / a
        #V_f^2 = V_i^2 + 2a∆x
        if isinstance(V_i, float) and isinstance(a, float) and isinstance(x, float) :
            V_f = sqrt(V_i**2 + 2 * a * x)
        elif isinstance(V_f, float) and isinstance(a, float) and isinstance(x, float) :
            V_i = sqrt(V_f**2 - 2 * a * x)
        elif isinstance(V_f, float) and isinstance(V_i, float) and isinstance(x, float) :
            a = (V_f**2 - V_i**2) / (2 * x)
        elif isinstance(V_f, float) and isinstance(V_i, float) and isinstance(a, float) :
            x = (V_f**2 - V_i**2) / (2 * a)
        #∆x = V_it + at^2
        if isinstance(V_i, float) and isinstance(t, float) and isinstance(a, float) :
            x = V_i * t + a * t**2
        elif isinstance(x, float) and isinstance(t, float) and isinstance(a, float) :
            V_i = x / t - a * t
        elif isinstance(x, float) and isinstance(V_i, float) and isinstance(t, float) :
            a = x / t - V_i
        elif isinstance(x, float) and isinstance(V_i, float) and isinstance(a, float) :
            t = (-V_i + sqrt(V_i**2 - 4 * x * a)) / (2 * a)
        #∆x = (V_i + V_f)t/2
        if isinstance(V_i, float) and isinstance(V_f, float) and isinstance(t, float) :
            x = (V_i + V_f) * t / 2
        elif isinstance(x, float) and isinstance(V_f, float) and isinstance(t, float) :
            V_i = 2 * x - V_f * t
        elif isinstance(x, float) and isinstance(V_i, float) and isinstance(t, float) :
            V_f = (2 * x - V_i) / t
        elif isinstance(x, float) and isinstance(V_i, float) and isinstance(V_f, float) :
            t = 2 * x / (V_i + V_f)
    if m == None :
        m = input("Enter m: ")
        if m != "" :
            try :
                m = float(m)
                if m <= 0 :
                    m = None
            except :
                m = None
        continue
    elif m != "" :
        print("m = " + str(m) + " kg")
    if unknowns > 2 :
        V_i = None
        t = None
        x = None
        a = None
        V_f = None
        unknowns = 0
        continue
    if a == None :
        a = input("Enter a: ")
        if a != "" :
            try :
                a = float(a)
            except :
                a = None
        else :
            unknowns += 1
        continue
    elif a != "" :
        print("a = " + str(a) + " m/s^2")
    if t == None :
        t = input("Enter t: ")
        if t != "" :
            try :
                t = float(t)
                if t <= 0 :
                    t = None
            except :
                t = None
        else :
            unknowns += 1
        continue
    elif t != "" :
        print("t = " + str(t) + " s")
    if x == None :
        x = input("Enter ∆x: ")
        if x != "" :
            try :
                x = float(x)
                if x <= 0 :
                    x = None
            except :
                x = None
        else :
            unknowns += 1
        continue
    elif x != "" :
        print("∆x = " + str(x) + " m")
    if V_i == None :
        V_i = input("Enter V_i: ")
        if V_i != "" :
            try :
                V_i = float(V_i)
                if V_i <= 0 :
                    V_i = None
            except :
                V_i = None
        else :
            unknowns += 1
        continue
    elif V_i != "" :
        print("V_i = " + str(V_i) + " m/s")
    if V_f == None :
        V_f = input("Enter V_f: ")
        if V_f != "" :
            try :
                V_f = float(V_f)
                if V_f <= 0 :
                    V_f = None
            except :
                V_f = None
        else :
            unknowns += 1
        continue
    elif V_f != "" :
        print("V_f = " + str(V_f) + " m/s")
    break
if (isinstance(m, float)) :
    print("p_i = " + str(m * V_i) + " kg m/s")
    print("p_f = " + str(m * V_f) + " kg m/s")
    print("E = " + str(m * V_f**2 / 2) + " J")
    print("P = " + str(m * V_f**2 / (2 * t)) + " W")