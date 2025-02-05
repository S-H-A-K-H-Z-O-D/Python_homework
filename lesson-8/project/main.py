
# Absolute imports
import ecommerce.products
product = ecommerce.products.Product()

# or
from ecommerce.products import Product
product = Product()

# or

from ecommerce import products
product = products.Product()

# from .ecommerce import contact

print('done')
