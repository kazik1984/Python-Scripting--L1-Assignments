def isListOfInts(list_of_elements):
    if len([x for x in list_of_elements if type(x) != int]) != 0 :
        return False
    else:
        return True


def testList(list_to_be_tested):
    try:
        if type(list_to_be_tested) == list:
            is_list_of_ints = isListOfInts(list_to_be_tested)
            printed_output = str(list_to_be_tested) + ' --> ' + str(is_list_of_ints)
            print(printed_output)
        else:
            raise ValueError
    except ValueError:
        print('ValueError: '+ str(list_to_be_tested) + '- arg not of <list> type')

if __name__ == '__main__':
    testList([])
    testList([1])
    testList([1,2])
    testList([0])
    testList(['1'])
    testList([1,'a'])
    testList(['a',1])
    testList([1,1.])
    testList([1.,1.])
    testList((1,2))

