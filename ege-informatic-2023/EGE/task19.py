from functools import lru_cache
def moves(h):
    a,b =h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

@lru_cache(None)
def game(h):
    a,b=h
    if a+b>=259: return 'W'
    if any(game(m)=='W' for m in moves(h)): return 'P1'
    if all(game(m)=='P1' for m in moves(h)): return 'B1'
    if any(game(m)=='B1' for m in moves(h)): return 'P2'
    if all((game(m)=='P2') or (game(m)=='P1') for m in moves(h)): return 'B2'

cnt=0
for s in range(1,242):
    h=17,s
    if game(h) =='B2':
        print(s,game(h))


        
#        cnt+=1

#print(cnt)
#print(s,game(s))
