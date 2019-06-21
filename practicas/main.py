
clients = 'axel,fernando'


def createCliente(clientName):
    # global nos permite usar variables que se crearon fuera de la función.
    global clients
    
    if clientName not in clients:
        _addComma()
        clients += clientName
    else:
        print('Client alredy is in the client\'s list')



def _addComma():
    global clients
    clients += ','


def listClients():
    global clients
    print(clients)


def _printWelcome():
    print('Welcome to Platzi sales')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C] Create client')
    print('[D] Delete client')


if __name__== '__main__':

    _printWelcome()
    command = input().upper()

    if command == 'C':
        clientName =  input('What\'s  the client name? ')
        createCliente(clientName)
        listClients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')