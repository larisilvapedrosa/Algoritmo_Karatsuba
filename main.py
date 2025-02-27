def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    max_digits = max(len(str(num1)), len(str(num2)))
    half_digits = max_digits // 2  

    superior1, inferior1 = divmod(num1, 10**half_digits)
    superior2, inferior2 = divmod(num2, 10**half_digits)

    prod_inferior = karatsuba(inferior1, inferior2)
    prod_soma = karatsuba(inferior1 + superior1, inferior2 + superior2)
    prod_superior = karatsuba(superior1, superior2)

    return (prod_superior * 10**(2 * half_digits)) + ((prod_soma - prod_superior - prod_inferior) * 10**half_digits) + prod_inferior

if __name__ == "__main__":
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print("Resultado algoritmo Karatsuba:", karatsuba(numero1, numero2))
