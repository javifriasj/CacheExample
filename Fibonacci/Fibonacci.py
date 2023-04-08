import functools

class Fibonacci:
    def counter(function):
        """
        Contador de llamadas para realizar el metodo de Fibonacci
        """
        function.calls = 0
        @functools.wraps(function)
        def _counter(*args, **kwargs):
            function.calls += 1
            return function(*args, **kwargs)
        return _counter
    
    @functools.lru_cache(maxsize=3) #Cache
    @counter
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return Fibonacci.fibonacci(n-1) + Fibonacci.fibonacci(n-2)