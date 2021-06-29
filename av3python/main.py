
import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Atv"
)
if mydb.is_connected():
    db_info = mydb.get_server_info()
    print("Connected.")

class Valores():
    def _init_(self, var, nums):
        self.var = int(var)
        self.nums = dict(nums)

def suv(valores, num):
    print(f'numero do Somatório = {num}')
    b = 0
    var_adc = 0
    for e in valores:
        var_adc += e['var'] * e['nums'][num]
    return round(var_adc + b, 2)


def esp(var_obitido, var_ideal):
    return round(((var_obitido - var_ideal) ** 2), 2)

def osp(esp,cont):
        return round((esp / cont), 2)

def usp(osps, esps):
 return round((osps - esps), 2)


def criar_nums(var):
    nums = {}
    for n_num in range(var):
        nums[f'w{n_num}'] = round(random.random(), 2)
    return nums


def cria_lista_valores(qtd_valores, qtd_nums_por_valores):
    valores = []
    for n_valores in range(qtd_valores):
        vars()[f'e{str(n_valores)}'] = {
            "nome": f'Valores {str(n_valores)}',
            "var": round(random.random(), 2),
            "nums": criar_nums(qtd_nums_por_valores)
        }
        valores.append(vars()[f'e{str(n_valores)}'])
    return valores

#/def odernar_valores(valores):
    #ordenar = sorted(valores)
    #return ordenar

def pull_num_randomico(valores):
    return f'w{str(random.randint(0, len(valores["nums"]) - 1))}'


def pull_nums_randomico(var):
    return f'w{str(random.randint(0, int(var) - 1))}'


def print_lista_valores(valores):
    for obj in valores:
        print(f'{obj["nome"]}: var = {obj["var"]}, nums = {obj["nums"]} ')

    print('\n')

def print_lista_valores_total(valores):
    for obj in valores:
        print(obj)
    print("\n")


def run():
    qtd_valores = 10
    qtd_nums = 10

    print(f'Valores: {qtd_valores}\nNums por valor: {qtd_nums}\n')

    valores = cria_lista_valores(qtd_valores, qtd_nums)
    #order = odernar_valores(valores)

    print_lista_valores(valores)

    adcs = suv(valores, pull_nums_randomico(qtd_nums))
    #udcs = suv(order, pull_nums_randomico(qtd_nums))

    print(f'Somas= {suv}')

    esps = esp(adcs, 1)

    print(f'Custos= {esps}')

    osps = osp(adcs, 2)

    print('tentativa de balanceamento automatica')
    print(f'Balanceamento= {osps}')

    usps = usp(osps, esps)
    print(f'diferenciacao= {usps}')
    
    #print(f'reordenacao = {udcs}')

    mycursor = mydb.cursor()

    sql = "INSERT INTO valores (nums, suv, esps) VALUES (%s, %s, %s)"
    val = [(esps, osps, usps)]
    mycursor.executemany(sql, val)
    mydb.commit()
    print("Dados Salvos")


if __name__ == '__main__':
    run()

