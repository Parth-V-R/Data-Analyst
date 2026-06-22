# We have prices of product and have to apply 10% discount to every product
import numpy as np
price=np.array([100,200,300])
discount=10

#here array "price" is operated upon,and resultant array is stored into
#final_price
final_price= price - (price*discount/100)
#Now final_price stores an resultant array
print(final_price)