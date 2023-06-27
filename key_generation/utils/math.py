def modInverse(e, t) :
        e = e % t;
        for x in range(1, t) :
            if ((e * x) % t == 1) :
                return x
        return 1