def most_frequent(s):
    ll=[]
    lc=[]
    for i in s:
      if i not in ll:
            ll.append(i)
            lc.append(s.count(i))
    while len(ll)>0:
        print(ll[lc.index(max(lc))],"=",(max(lc)))
        ll.pop(lc.index(max(lc)))
        lc.pop(lc.index(max(lc)))
a=input("Please enter a String :")
most_frequent(a)
