def add_code_block(file_path, code_block):
    with open(file_path, 'a') as file:
        file.write(code_block)

# Ejemplo de uso
file_path = 'pulumi/aws/__main__.py'
code_block = '''
# Aquí va tu bloque de código
def mi_funcion():
    print("Hola, mundo!")
'''

add_code_block(file_path, code_block)