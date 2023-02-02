from trojkat import Trojkat
from Prostokat import  Prostokat

tr = Trojkat(4,5.5)
print(f"pole figury: {tr.__class__.__name__} wynosi {tr.policz_pole():.2f} cm2")

pr1 = Prostokat(6.1,3.8)
pr2 = Prostokat(5.5,5.5)
print(f"pole figury: {pr1.__class__.__name__} wynosi {pr1.policz_pole():.2f} cm2")
print(f"pole figury: {pr2.__class__.__name__} wynosi {pr2.policz_pole():.2f} cm2")





