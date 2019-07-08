import sys

clients = ['pablo','ricardo']

#Funcion crear cliente
def create_client(client_name):
    
    if client_name not in clients:
        clients.append(client_name)
        
    else:
        print('Client already is in the client\'s list')

#Funcion para listar los clientes
def list_clients():
    for idx, client in enumerate(clients):
        print('{}:,{}'.format(idx, client))

    print(clients)
#Funcion para actualizar un cliente de la lista
def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        return client_notin_list()

#Funcion para eliminar cliente de la lista
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        return client_notin_list()

def search_client(client_name):
    
    for client in clients:
        if client != client_name:
            continue
        else:
            return True



# Funcion que imprime que los clients no estan en la lista
def client_notin_list(client_name):
    if client_name not in clients:
        print ('Client is not in clients list')
    
''' #Agregando una coma
def _add_comma():
    global clients

    clients += ',' '''

# imprime opciones que posteriormente se usaran
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print('[L]ist client')
    print ('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
#Funcion que permite introducir datos
def _get_client_name():
    client_name = None

    while not client_name:
        client_name= raw_input('What is the client name?')
    if client_name == 'exit':
        sys.exit()            
    return client_name
    print('create other client? Y or N')

    




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
    elif command == 'L':
        list_clients()
    elif command == 'U':
        list_clients()
        client_name= _get_client_name()
        updated_client_name = raw_input('What is the updated client name')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        list_clients()
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client es in the clien\'s list')
        else:
            print('The client: {} is not in our client\'s '.format(client_name))


    else:
        print('Invalid command')

