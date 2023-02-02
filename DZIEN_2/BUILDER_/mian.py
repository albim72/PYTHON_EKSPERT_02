from builder import Builder
from director import Director
from concrete_builder1 import  ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Podstawowy produkt:")
director.build_minimal_variable_produkt()
builder.product.list_parts()
print("\n")

print("Pełny produkt:")
director.build_full_featured_product()
builder.product.list_parts()
print("\n")

print("Produkt -> werja zmieniona:")
builder.product_part_a()
builder.product_part_c()
builder.product.list_parts()
print("\n")
