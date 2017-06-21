# somemodule.py

def spam():
    print("call spam")

def grok():
    print("call grok")

blah = 42

# Only export 'spam' and 'grok'
__all__ = ['spam']