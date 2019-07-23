#cambiando la lista por un diccionario de clients
#clients = ['pablo','ricardo']
clients = [
    {
        'name':'Pablo',
        'company':'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'


    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Web design'

    }]

#Funcion crear cliente
def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)

    else:
        print('Client already is in the client\'s list')

#Funcion para listar los clientes
def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
            ))

#Funcion para actualizar un cliente de la lista
def update_client(client, updated_client):
    global clients

    if client in clients:
        index = clients.index(client)
        clients[index] = updated_client
    else:
        return client_notin_list()

#Funcion para eliminar cliente de la lista
def delete_client(client):
    global clients

    if client in clients:
        clients.remove(client)
    else:
        return client_notin_list()

def search_client(client):

    for client in clients:
        if client != clients:
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

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field

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

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()


    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),

        }
        create_client(client)
        list_clients()
    elif command == 'D':
        list_clients()
        client = _get_client_field()
        delete_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        list_clients()
        client = _get_client_field()
        updated_client = input('What is the updated client name')
        update_client(client, updated_client)
        list_clients()
    elif command == 'S':
        list_clients()
        client = _get_client_field()
        found = search_client(client)

        if found:
            print('The client es in the clien\'s list')
        else:
            print('The client: {} is not in our client\'s '.format(client))


    else:
        print('Invalid command')

