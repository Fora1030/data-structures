"""
pythonic special method names categories.
---
    Attribute Access: 

"""
class Card:
    def  __init__( self, rank, suit ):
        self.suit= suit
        self.rank= rank
        self.hard, self.soft = self._points()
class NumberCard( Card ):
    def _points( self ):
        return int(self.rank), int(self.rank)
class AceCard( Card ):
    def _points( self ):
        return 1, 11
    def __repr__(self) -> str:
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(
            __class__ = self.__class__, **self.__dict__
        )
class FaceCard( Card ):
    def _points( self ):
        return 10, 10


class Suit:
    def __init__( self, name, symbol ):
        self.name= name
        self.symbol= symbol

# Using factory design pattern 
Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')

def card(rank, suit):
    if rank ==1: return AceCard('A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12:'Q', 13:'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Rank out of range")

# Using mapping and class objects
def card1( rank, suit ):
    class_= {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return class_( rank, suit )

# Partial function solution
# from functools import partial, cmp_to_key, reduce

# def card2( rank, suit ):
#     part_class = {
#         1: partial(AceCard,'A'),
#         11: partial(FaceCard,'J'),
#         12: partial(FaceCard,'Q'),
#         13: partial(FaceCard,'K'),
#     }.get(rank, partial(NumberCard, str(rank)))
#     return part_class(suit)

# deck = [card2(rank, suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade)]
# print([f"{item.suit.name}, {item.rank}, {item.suit.symbol}" for item in deck])

class CardFactory:
    def rank( self, rank ):
        self.class_, self.rank_str= {
            1:(AceCard,'A'),
            11:(FaceCard,'J'),
            12:(FaceCard,'Q'),
            13:(FaceCard,'K'),
            }.get(rank, (NumberCard, str(rank)))
        return self
    def suit( self, suit ):
        return self.class_( self.rank_str, suit )
    
    def __repr__(self) -> str:
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(
            __class__ = self.__class__, **self.__dict__
        )

card8 = CardFactory()
deck8 = [card8.rank(r+1).suit(s) for r in range(13) for s in (Club, Diamond, Heart, Spade)]
# print([ obj.__repr__() for obj in deck8])
# print([card.suit.symbol for card in deck8])
# def cmp_fun(a, b):
#     print(f"a:{a}, b:{b}")
#     print(f"a[0]:{a[0]}, b[0]:{b[0]}")
    # if a[0] > b[0]:
    #     return 1
    # elif a[0] < b[0]:
    #     return -1
    # else:
    #     return 0

# list1 = ['geeks', 'for', 'geeks', 'z']
# l = sorted(list1, key=cmp_to_key(cmp_fun))
# print(l)

# using reduce
# list1 = [2,4,7,9,1,3]
# sum_of_list1 = reduce(lambda a, b: a*b, list1)

# print(sum_of_list1)
# from functools import total_ordering

# @total_ordering
# class N:
#     def __init__(self, value) -> None:
#         self.value = value

#     def __eq__(self, other: object) -> bool:
#         return self.value == other.value

#     def __lt__(self, other: object) -> bool:
#         return self.value > other.value

# print('6 > 2:', N(6)>N(2))
# print('3 < 1:', N(3)<N(1))
# print('2 <= 7:', N(2)<=N(7))
# print('9 >= 10:', N(9)>=N(10))
# print('5 == 5:', N(5)==N(5))
# def to_upper_test(str_test):
#     return str(str_test).upper()
# c = [ 
#     "one",
#     "Two",
#     "three",
#     "four",
#     "five",
#     "six",
# ]

# print(", ".join(map(to_upper_test, c)))

class Float_Units(float):
    # def __init__(self, value, unit) -> None: # immutable object can not be changed using __init__
    def __new__(cls, value, unit):
        obj = super().__new__(cls, value)
        obj.unit = unit
        return obj

Useless = type('Useless', (), {})
print(Useless)