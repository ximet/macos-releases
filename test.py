from main import getMacOSRelease

def test_getMacOS():
    assert getMacOSRelease("18.2.0") == ('Mojave', '10.14.1')

def test_getBetaMacOS():
    assert getMacOSRelease("20.0.0") == ('Big Sur', '11.0 beta 1')

def test_firstRelease():
    assert getMacOSRelease("5.1") == ('Puma', '10.1.1')


# def test_getMyMacOS():
#     assert getMacOSRelease("") == ('Catalina', '10.15.5')