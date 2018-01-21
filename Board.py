from random import shuffle
import Piece

class Board(object):

    def __init__(self, shuffle_market = False):
        self.board = range(54)
        self.board_income = [4.5, 10.5, 16.5, 22.5, 28.5, 34.5,40.5, 46.5,52.5]
        self.board_patches = [25.5, 31.5, 37.5, 43.5, 49.5]
        self.market = []
        self.PATCH = Piece.Piece('patch',1,0,0,0)
        self.LENGTH = 53

        self.market.append( Piece.Piece('3/1 elbow',3,0,3,1))
        self.market.append( Piece.Piece('10/5 stub',6,3,10,5))
        self.market.append( Piece.Piece('1/3 elbow',3,0,1,3))
        self.market.append( Piece.Piece('3/2 zig',4,1,3,2))
        self.market.append( Piece.Piece('4/2 l',4,1,4,2))
        self.market.append( Piece.Piece('10/3 l',5,2,10,3))
        self.market.append( Piece.Piece('3/3 line',4,1,3,3))
        self.market.append( Piece.Piece('2/2 stub',5,0,2,2))
        self.market.append( Piece.Piece('8/6 blob',6,3,8,6))
        self.market.append( Piece.Piece('6/5 square',4,2,6,5))
        self.market.append( Piece.Piece('2/3 long-s',5,1,2,3))
        self.market.append( Piece.Piece('1/5 u',6,1,1,5))
        self.market.append( Piece.Piece('7/4 hump',6,2,7,4))
        self.market.append( Piece.Piece('5/4 t',5,2,5,4))
        self.market.append( Piece.Piece('5/5 t',5,2,5,5))
        self.market.append( Piece.Piece('4/6 l',4,2,4,6))
        self.market.append( Piece.Piece('4/2 fat-stair',6,0,4,2))
        self.market.append( Piece.Piece('5/3 blob',8,1,5,3))
        self.market.append( Piece.Piece('3/4 half-t',5,1,3,4))
        self.market.append( Piece.Piece('0/3 cross',6,1,0,3))
        self.market.append( Piece.Piece('2/3 h',7,0,2,3))
        self.market.append( Piece.Piece('7/6 zig',4,3,7,6))
        self.market.append( Piece.Piece('2/2 half-t',4,0,2,2))
        self.market.append( Piece.Piece('1/4 cross',7,1,1,4))
        self.market.append( Piece.Piece('10/4 stair',5,3,10,4))
        self.market.append( Piece.Piece('2/2 line',3,0,2,2))
        self.market.append( Piece.Piece('1/2 u', 5,0,1,2))
        self.market.append( Piece.Piece('7/1 line', 5,1,7,1))
        self.market.append( Piece.Piece('2/1 weird',6,0,2,1))
        self.market.append( Piece.Piece('3/6 fighter',6,2,3,6))
        self.market.append( Piece.Piece('1/2 tall-s',6,0,1,2))
        self.market.append( Piece.Piece('7/2 t',6,2,7,2))
        self.market.append( Piece.Piece('2/1 line', 2,0,2,1))

        if shuffle_market:
            shuffle(self.market)
            
    def remove_piece_from_market(self, ix):
        self.market = self.market[ix+1:] + self.market[:ix]
        
    def print_market(self, n=3):
        print('Market:')
        if n<=3:
            for p in self.market[:n]:
                print( '\t{}, b:{}, s:{}'.format(p.name,p.buttons,p.squares))
        if n>=4:
            for p in self.market[:3]:
                print( '\t{}, b:{}, s:{}'.format(p.name,p.buttons,p.squares))
            for p in self.market[3:n]:
                print( '\t+{}, b:{}, s:{}'.format(p.name,p.buttons,p.squares))

    def print_whole_market(self):
        for p in self.market:
                print( '\t{}, b:{}, s:{}'.format(p.name,p.buttons,p.squares))

    def reset(self):
        self.__init__(shuffle_market=True)

