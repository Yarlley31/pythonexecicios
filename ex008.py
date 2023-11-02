m = float(input('Insira um valor em metros: '))
# km hm dam m dm cm mm
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print(f'A medida {m} correponde à: \n {km:.6f}km; \n {hm:.6f}hm; \n {dam:.6f}dam; \n {dm:.0f}dm; \n {cm:.0f}cm; \n {mm:.0f}mm.')