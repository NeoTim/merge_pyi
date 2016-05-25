# Copyright (c) 2016 Google Inc. (under http://www.apache.org/licenses/LICENSE-2.0)
def f1(x : e1) -> r1: ...

def f2(x) -> r2: ...

def f3(x : e3): ...

def f4(x : e4 = d4) -> r4: ...

def f5(x :             # stripme
    e5) -> r5: ...

#trailing comma
def f6(x : e6,) -> r6: ...

def f7(x : e7          # stripme
    ) -> r7: ...

def f8(    \
     x     \
     :     \
     e8    \
     )     \
     ->    \
     r8:   \
     ...

def f9(a) -> """
this is 
valid""" : ...

def f10(a: """
this is 
valid""") : ...
