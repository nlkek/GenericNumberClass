def convert_to_base(num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return convert_to_base(n // to_base, to_base) + alphabet[n % to_base]
    

def create_number_class(alphabet):

    class num_class:
        
        base = len(alphabet)
        
        def __init__(self, num):
            self.num = int(convert_to_base(num, 10, self.base))
                        
        def __str__(self):
            return convert_to_base(self.num, self.base, 10)
        
        def __add__(self, obj):
            return num_class(self.num + obj.num)
        
        def __sub__(self, obj):
            return num_class(self.num - obj.num)
        
        def __mul__(self, obj):
            return num_class(self.num * obj.num)
        
        def __floordiv__(self, obj):
            return num_class(self.num // obj.num)

        def convert_to(self, num_class):
            return num_class(self.num)
        
    return num_class
        
    
