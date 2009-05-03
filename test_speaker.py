from speaker import *

def test_replace_bad_symbols():
    test = '()?.aodd,"\'[]:;@#$%^&aoeu*+><_/`~='
    assert replace_bad_symbols(test) == '    aodd             aoeu         '

def test_replace_links():
    assert replace_links('Take a look at http://google.com. I like it') == 'Take a look at link. I like it'
    assert replace_links('New version ftp://example.com/sketch.tar.bz. Check it please') == 'New version link. Check it please'
