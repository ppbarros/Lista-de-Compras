from control import Control
from view import View
from model import Model


m = Model()
v = View()
c = Control(v, m)
v.set_control(c)
v.exibir_menu()