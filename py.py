print ("Bem-vindo a loja de Emanuelle Annemann Silva ")

print("\nResumo do pedido")
produto = int(input("quantidade do produto:"))
valor_unitário = float(input("Valor unitário do produto:"))

valor_sem_desconto = produto * valor_unitário
if valor_sem_desconto >= 25000:
    valor_do_desconto = 0
    desconto = 0

elif valor_sem_desconto >= 25000 and valor_sem_desconto <6000:
    valor_do_desconto = 0.04 * valor_sem_desconto
    desconto = 4

elif valor_sem_desconto >= 6000 and valor_sem_desconto <10000:
    valor_do_desconto = 0.07 * valor_sem_desconto
    desconto = 7

elif valor_sem_desconto >= 10000:
    valor_do_desconto = 0.11 * valor_sem_desconto
    desconto = 11
else:
    desconto = 0


valor_com_desconto = valor_sem_desconto - valor_do_desconto

print(f"Valor total sem desconto: R$ {valor_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto}% ")
print(f"Valor do desconto: R$ {valor_do_desconto:}")
print(f"Valor total a pagar: R$ {valor_com_desconto:.2f}")

print("\nObrigado por comprar conosco!")
