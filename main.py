from yapf.yapflib.py3compat import raw_input

clients = 'pablo,ricardo,'

#Funcion crear cliente
def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')

#Funcion para listar los clientes
def list_clients():
    global clients

    print(clients)
#Funcion para actualizar un cliente de la lista
def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',' , updated_client_name + ',')
    else:
        return client_notin_list()

#Funcion para eliminar cliente de la lista
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        return client_notin_list()

# Funcion que imprime que los clients no estan en la lista
def client_notin_list(client_name):
    if client_name not in clients:
        print ('Client is not in clients list')
    
#Agregando una coma
def _add_comma():
    global clients

    clients += ','

# imprime opciones que posteriormente se usaran
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print ('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
#Funcion que permite introducir datos
def _get_client_name():
    return raw_input('What is the client name?')


if __name__ == '__main__':
    _print_welcome()
    
    command = raw_input()
    command = command.upper()


    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        list_clients()
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        list_clients()
        client_name= _get_client_name()
        updated_client_name = raw_input('What is the updated client name')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name():

    else:
        print('Invalid command')

