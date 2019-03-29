# a class of all the CodeWars exercise
class CodeWars:
    def __init__(self):
        self.age = 23

    def spin_words(self, sentence):
        '''
        function that takes in a string of one or more words, and returns the same string,
        but with all five or more letter words reversed.
        Examples:
        spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
        spinWords( "This is a test") => returns "This is a test"
        spinWords( "This is another test" )=> returns "This is rehtona test"
        '''

        my_list = []
        for item in sentence.split():
            if len(item) >= 5:
                my_list.append(item[::-1])
            else:
                my_list.append(item)

        return ' '.join(my_list)

    def narcissistic(self, value):

        """
        A Narcissistic Number is a number which is the sum of its own digits, each raised to the power
        of the number of digits in a given base.
        For example, take 153 (3 digits):
            1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
        and 1634 (4 digits):
            1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
        """
        total = 0
        num_list = [int(i) for i in str(value)]
        for item in num_list:
            total += item**int(len(str(value)))

        if total == value:
            return True
        else:
            return False

    def countBits(self, n):
        """
        function that takes an integer as input, and returns the number of bits that are
        equal to one in the binary representation of that number. You can guarantee that input is non-negative.

        Example: The binary representation of 1234 is 10011010010, so the function should return 5
        in this case
        """

        num_list = [int(i) for i in bin(n)[2:] if int(i) == 1]
        return sum(num_list)

    def panagram(self, sentence):
        """
        A panagram is a sentence that contains every single letter of the alphabet at least once.
        For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because
        it uses the letters A-Z at least once (case is irrelevant).

        Given a string, detect whether or not it is a panagram. Return True if it is, False if not.
        Ignore numbers and punctuation.
        """
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        return all([i in sentence.lower() for i in alphabets])







    '''
    function, persistence, that takes in a positive parameter
    num and returns its multiplicative persistence, which is the number
    of times you must multiply the digits in num until you reach a single
    digit.

     persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                           # and 4 has only one digit.

     persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                           # 1*2*6 = 12, and finally 1*2 = 2.

     persistence(4) => 0   # Because 4 is already a one-digit number.'''


    #my Code
    '''def persistence(m, count=0 ):
        total=1

        if len(str(m)) == 1 or m < 0:
            return num_times
        else:
            for i in list(str(m)):
                total *= int(i)
            count +=1


        if len(str(total)) > 1:
            return persistence(total,count)



        elif len(str(total)) == 1:
            #print('The Persistence equals %d'%(int(total)))
            return count
     '''

    def persistence(self, n):
        n = str(n)
        count = 0
        while len(n) > 1:
            p = 1
            for i in n:
                p *= int(i)
            n = str(p)
            count += 1
        return count






    def namelist(self, names):
        '''
        Given: an array containing hashes of names
        Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
        example:
        namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
        # returns 'Bart, Lisa & Maggie'

        namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
        # returns 'Bart & Lisa'

        namelist([ {'name': 'Bart'} ])
        # returns 'Bart'

        namelist([])
        # returns ''
        '''

        if len(names) > 1:
            return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                    names[-1]['name'])
        elif names:
            return names[0]['name']
        else:
            return ''
