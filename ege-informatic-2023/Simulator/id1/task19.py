
from functools import lru_cache
def move(h):
    a,b=h
    return (a-1,b),(a,b-1),(a//2,b),(a,b//2)

@lru_cache
def game(h):
    a,b=h
    if a+b<=21: return 'W'
    if any(game(m)=='W' for m in move(h)): return 'P1'
    if all(game(m)=='P1' for m in move(h)): return 'B1'
    if any(game(m)=='B1' for m in move(h)): return 'P2'
    if all((game(m)=='P1')or(game(m)=='P2') for m in move(h)): return 'B2'

for s in range(100,10):
    a=7
    b=s
    h=a,b
    if game(h)=='P2':
        print(s,game(h))

