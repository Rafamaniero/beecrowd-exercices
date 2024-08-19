pi = 3.14159
raio = float(input("raio="))
area = pi*(raio**2)
format_area = str("%.4f" % round(area,4))
print("A=" + format_area)