class Control:
    def __init__(self, view, model):
        self.model = model
        self.view = view
    def exibir_menu(self):
        self.view.exibir_menu()
    def get_lista_compras(self):
        return self.model.get_lista_compras()
    def incluir_item(self, item, quant):
        if item in self.model.get_lista_compras().keys():
            quant_produto = self.model.get_lista_compras()[item]
            quant_produto += quant
            self.model.get_lista_compras()[item] = quant_produto
        else:
            self.model.get_lista_compras()[item] = quant
    def excluir_item(self, item):
        if item in self.model.get_lista_compras().keys():
            self.model.get_lista_compras().pop(item)