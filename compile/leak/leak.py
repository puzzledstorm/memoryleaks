from ctypes import CDLL

def leak():
    leak = CDLL('./leak.so')
    n = 100
    if hasattr(leak, "leak"):
        leak.leak(n)
        print(f"leak memory {n}M")
 
if __name__ == "__main__":
    leak()

# python -u /workspaces/memoryleaks/compile/leak/leak.py