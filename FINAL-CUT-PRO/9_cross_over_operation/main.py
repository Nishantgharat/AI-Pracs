import random
import math
def main():
    str1 = input("Enter 1st gene : ")
    str2 = input("Enter 2nd gene : ")
    gene1 = list(str1)
    gene2 = list(str2)
    n = len(gene1)
    k = math.floor(random.random() * n)
    print(f"Crossover point is: {k}")
    final_genes = list()
    index = 0
    while index < n:
        if index < k:
            final_genes.append(gene1[index])
        else:
            final_genes.append(gene2[index])
        index += 1
    final_str = ""
    for bit in final_genes:
        final_str += bit
    print(str1)
    print(str2)
    print("Offspring1:  ",final_str)

    final_genes = list()
    index = 0
    while index < n:
        if index < k:
            final_genes.append(gene2[index])
        else:
            final_genes.append(gene1[index])
        index += 1
    final_str = ""
    for bit in final_genes:
        final_str += bit
    print(str1)
    print(str2)
    print("offspring2:  ",final_str)
main()