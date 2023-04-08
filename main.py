from Fibonacci.Fibonacci import Fibonacci
from datetime import datetime

start_time = datetime.now()
for i in range(1, 1000):
    print('Fibonacci %d: %d' % (i, Fibonacci.fibonacci(i)))
end_time = datetime.now()

print(end_time - start_time)
print(Fibonacci.fibonacci.__wrapped__.__wrapped__.calls)