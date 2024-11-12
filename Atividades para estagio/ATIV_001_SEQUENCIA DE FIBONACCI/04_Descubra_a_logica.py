# Sequência a: 1, 3, 5, 7, ___
def sequencia_a():
    seq = [1, 3, 5, 7]
    proximo_elemento = seq[-1] + 2
    seq.append(proximo_elemento)
    return seq

# Sequência b: 2, 4, 8, 16, 32, 64, ____
def sequencia_b():
    seq = [2, 4, 8, 16, 32, 64]
    proximo_elemento = seq[-1] * 2
    seq.append(proximo_elemento)
    return seq

# Sequência c: 0, 1, 4, 9, 16, 25, 36, ____
def sequencia_c():
    seq = [0, 1, 4, 9, 16, 25, 36]
    proximo_elemento = (len(seq))**2
    seq.append(proximo_elemento)
    return seq

# Sequência d: 4, 16, 36, 64, ____
def sequencia_d():
    seq = [4, 16, 36, 64]
    proximo_elemento = (len(seq) * 2 + 2)**2
    seq.append(proximo_elemento)
    return seq

# Sequência e: 1, 1, 2, 3, 5, 8, ____
def sequencia_e():
    seq = [1, 1, 2, 3, 5, 8]
    proximo_elemento = seq[-1] + seq[-2]
    seq.append(proximo_elemento)
    return seq

# Sequência f: 2, 10, 12, 16, 17, 18, 19, ____
def sequencia_f():
    seq = [2, 10, 12, 16, 17, 18, 19]
    proximo_elemento = seq[-1] + 1
    seq.append(proximo_elemento)
    return seq

# Impressão das sequências com os próximos elementos
print("Sequência a:", sequencia_a())
print("Sequência b:", sequencia_b())
print("Sequência c:", sequencia_c())
print("Sequência d:", sequencia_d())
print("Sequência e:", sequencia_e())
print("Sequência f:", sequencia_f())