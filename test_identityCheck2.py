# TESTATAAN MODUULIN identityCheck2.py LUOKKIEN TOIMINTAA

import identityCheck2

testSsnOK = identityCheck2.NationalSSN('130728-478N')
testSsnShort = identityCheck2.NationalSSN('130728-78N')   
testSsnOK = identityCheck2.NationalSSN('1300728-478N')

def test_checkSsnLengthOk():
    assert testSsnOK.checkSsnLengthOk() == True
    assert testSsnShort.checkSsnLengthOk() == False
    assert testSsnLong.checkSsnLengthOk() == False
    