from ctypes import CDLL

def leak():
    # leak = CDLL('./leak.so')
    leak = CDLL('/workspaces/memoryleaks/compile/leak/leak.so')
    n = 2
    if hasattr(leak, "leak"):
        leak.leak(n)
        print(f"leak memory {n}M")
 
if __name__ == "__main__":
    leak()

# python -u /workspaces/memoryleaks/compile/leak/leak.py