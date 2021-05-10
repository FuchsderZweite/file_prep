class Progress_bar:
    len = 30
    
    def __init__(self, num, max_num):
        self.num = num
        self.max_num = max_num
        if self.num > self.max_num:
            print('The input values are not valid. Swapped arguments (numerator/denominator)? \n'
                  'Progress bar is therefore meaningless.')
            self.num = 1
            self.max_num = 1
            self.percent = self.num / self.max_num
        else:
            self.percent = self.num / self.max_num

    def show_bar(self):
        perc = round(self.percent * 100)
        print(']' + self.num*'#' + (self.max_num-self.num)*' ' + '[ {}%'.format(perc))
