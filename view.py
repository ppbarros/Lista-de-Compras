class View:
    def __init__(self):
        self.control = None
    def set_control(self, control):
        self.control = control
    def exibir_menu(self):
        resposta = True

        while resposta:
            print('''
1. Exibir lista
2. Incluir item
3. Excluir item
4. Sair
''')
            resposta = input('Digite um número: ')
            if resposta == '1':
                print('\nLista de itens')
                self.exibir_lista_de_compras()
            elif resposta == '2':
                item = input('\nDigite o item a ser incluído: ').lower().capitalize()
                quant = int(input('Digite a quantidade a ser adicionada: '))
                self.control.incluir_item(item, quant)
                print('\nItem incluído')
            elif resposta == '3':
                item = input('Digite o item a ser excluído: ').lower().capitalize()
                self.control.excluir_item(item)
                print('\nItem excluído')
            elif resposta == '4':
                print('\nTchau')
                resposta = False
            else:
                print('\nValor incorreto')
    def exibir_lista_de_compras(self):
        for p, q in self.control.get_lista_compras().items():
            print(f'''{p}: {q}''')