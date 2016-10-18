def a(*args, **kwargs):
    b(*args, **kwargs, error=True)
    
def b(*args, **kwargs):
    c(*args, **kwargs)
    
def c(*args, **kwargs):
    d(*args, **kwargs)

def d(error=False, *args, **kwargs):
    if error:
        raise Exception("Error condition!")

if __name__=="__main__":
    a()
