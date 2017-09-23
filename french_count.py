import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')
  

    f.add_state('1')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('8')
    f.add_state('9')
    f.add_state('10') 
    f.add_state('11')
    f.add_state('12')
    f.add_state('13')
    f.add_state('14')
    f.add_state('15')
    f.add_state('16')
    
    f.initial_state = '1'
    f.set_final('8')
    f.set_final('9')
    f.set_final('5')
    f.set_final('11')
    f.set_final('12')
    f.set_final('13')
    f.set_final('15')
    f.set_final('16')

    for num in xrange(10):
        if num == 1 :
            f.add_arc('1', '2', (str(num)), [kFRENCH_TRANS[100]])
        elif num == 0 :
            f.add_arc('1', '3',(str(num)), ())   
        elif num in [2,3,4,5,6,7,8,9] :
            f.add_arc('1', '2', (str(num)), [kFRENCH_TRANS[num]+' ' +kFRENCH_TRANS[100]])
            
        if num == 7:
            f.add_arc('3', '10', (str(num)), [kFRENCH_TRANS[60]])
        elif num == 9:
            f.add_arc('3', '7', (str(num)), [kFRENCH_TRANS[4]+' ' +kFRENCH_TRANS[20]])
        elif num == 1:
            f.add_arc('3', '7', (str(num)), ())
        elif num == 8:
            f.add_arc('3', '14', (str(num)), [kFRENCH_TRANS[4]+' '+kFRENCH_TRANS[20]]) 
        elif num == 0:
            f.add_arc('3', '4', (str(num)), ())   
        elif num in [2,3,4,5,6]: 
            f.add_arc('3', '6', (str(num)), [kFRENCH_TRANS[(num*10)]]) 
            
        if num == 0 :
            f.add_arc('14', '15', (str(num)), ())
        elif num in [1,2,3,4,5,6,7,8,9]:
            f.add_arc('14', '15', (str(num)), [kFRENCH_TRANS[(num)]])
            
        if num == 1:
            f.add_arc('10', '12', (str(num)), ['et' +' ' + kFRENCH_TRANS[(11)]])
        elif num in [0,2,3,4,5,6]:
            f.add_arc('10', '12', (str(num)), [kFRENCH_TRANS[(num+10)]])
        elif num in [7,8,9]:
            f.add_arc('10', '12', (str(num)), ['dix' + ' '+kFRENCH_TRANS[(num)]])
              
        if num == 1:
            f.add_arc('6', '16', (str(num)), ['et' +' ' + kFRENCH_TRANS[(1)]])
        elif num in [2,3,4,5,6,7,8,9]:
            f.add_arc('6', '16', (str(num)), [kFRENCH_TRANS[(num)]])
        elif num ==0:
            f.add_arc('6', '16', (str(num)), ())
            
        if num in [0,1,2,3,4,5,6]:
            f.add_arc('7', '8', (str(num)), [kFRENCH_TRANS[(num+10)]])
        elif num in [7,8,9] :
            f.add_arc('7', '8', (str(num)), ['dix' + ' '+kFRENCH_TRANS[(num)]])
            
        if num == 0:
            f.add_arc('4', '5', (str(num)), [kFRENCH_TRANS[(num)]])
        elif num in [1,2,3,4,5,6,7,8,9]:
            f.add_arc('4', '15', (str(num)), [kFRENCH_TRANS[(num)]])
            
        if num == 1:
            f.add_arc('2', '7', (str(num)), ())
        elif num == 9:
            f.add_arc('2', '7', (str(num)), [kFRENCH_TRANS[4]+' ' +kFRENCH_TRANS[20]])    
        elif num == 7 :
            f.add_arc('2', '10', (str(num)), [kFRENCH_TRANS[60]])
        elif num ==0:
            f.add_arc('2', '14', (str(num)), ())
        elif num == 8 :
            f.add_arc('2', '14', (str(num)), [kFRENCH_TRANS[4]+' '+kFRENCH_TRANS[20]])
        elif num in [2,3,4,5,6]:
            f.add_arc('2', '6', (str(num)), [kFRENCH_TRANS[(num*10)]])
        


    

    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
