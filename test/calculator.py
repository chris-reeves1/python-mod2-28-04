class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int,float)):
            raise TypeError("Custom Error: input should be numeric")
        return a + b