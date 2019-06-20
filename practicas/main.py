
clients = 'axel,fernando'


def crearCliente(clientName):
    # global nos permite usar variables que se crearon fuera de la función.
    global clients
    _addComma()
    clients += clientName


def _addComma():
    global clients
    clients += ','


def listClients():
    global clients
    print(clients)


if __name__== '__main__':
    listClients()
    crearCliente('ana')
    listClients()
