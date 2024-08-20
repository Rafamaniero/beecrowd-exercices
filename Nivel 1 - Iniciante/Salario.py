funcionario = int(input())
hrs = int(input())
vhr = float(input())
salario = hrs*vhr
format_salario = str("%.2f" % round(salario,2))
print("NUMBER =", funcionario)
print("SALARY = U$", format_salario)