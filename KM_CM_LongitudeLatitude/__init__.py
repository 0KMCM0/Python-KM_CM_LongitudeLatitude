from decimal import Decimal as _Decimal
from math import sin as _sin, cos as _cos, atan2 as _atan2, radians as _radians

class LongitudeLatitude:
    def __init__( self,
                  Longitude = '0',
                  Latitude = '0' ):
        self.m_flLongitude = _Decimal( Longitude )
        self.m_flLatitude = _Decimal( Latitude )

    def __getitem__( self, Index ):
        return self.m_flLongitude if Index == 0 else self.m_flLatitude
    def __setitem__( self, Index, Value ):
        if Index == 0: self.m_flLongitude = _Decimal( Value )
        else: self.m_flLatitude = _Decimal( Value )

    def Distance( self, Other, Diameter = 12756274 ):
        LT1R = _radians( self.m_flLatitude )
        LN1R = _radians( self.m_flLongitude )
        LT2R = _radians( Other.m_flLatitude )
        LN2R = _radians( Other.m_flLongitude )
        X = _sin( ( LT2R - LT1R ) * .5 ) ** 2 + _cos( LT1R ) * _cos( LT2R ) * _sin( ( LN2R - LN1R ) * .5 ) ** 2
        return _Decimal( Diameter ) * _Decimal( _atan2( X ** .5, ( 1 - X ) ** .5 ) )

    def __str__( self ): return f"{ abs( self.m_flLatitude ) }°{ 'S' if self.m_flLatitude < 0 else 'N' } { abs( self.m_flLongitude ) }°{ 'W' if self.m_flLongitude < 0 else 'E' }"
    def __repr__( self ): return f'LongitudeLatitude({ self.m_flLongitude },{ self.m_flLatitude })'

    def __Operator__( self, Other, Func ):
        if isinstance( Other, LongitudeLatitude ):
            return LongitudeLatitude( Func( self.m_flLongitude, Other.m_flLongitude ), Func( self.m_flLatitude, Other.m_flLatitude ) )
        return LongitudeLatitude( Func( self.m_flLongitude, _Decimal( Other ) ), Func( self.m_flLatitude, _Decimal( Other ) ) )

    def __ROperator__( self, Other, Func ):
        if isinstance( Other, LongitudeLatitude ):
            return LongitudeLatitude( Func( Other.m_flLongitude, self.m_flLongitude ), Func( Other.m_flLatitude, self.m_flLatitude ) )
        return LongitudeLatitude( Func( Other, self.m_flLongitude ), Func( Other, self.m_flLatitude ) )

    def __add__( self, Other ): return      self.__Operator__( Other, lambda A, B: A + B )
    def __sub__( self, Other ): return      self.__Operator__( Other, lambda A, B: A - B )
    def __mul__( self, Other ): return      self.__Operator__( Other, lambda A, B: A * B )
    def __pow__( self, Other ): return      self.__Operator__( Other, lambda A, B: A ** B )
    def __mod__( self, Other ): return      self.__Operator__( Other, lambda A, B: A % B )
    def __truediv__( self, Other ): return  self.__Operator__( Other, lambda A, B: A / B )
    def __floordiv__( self, Other ): return self.__Operator__( Other, lambda A, B: A // B )

    def __radd__( self, Other ): return      self.__ROperator__( Other, lambda A, B: A + B )
    def __rsub__( self, Other ): return      self.__ROperator__( Other, lambda A, B: A - B )
    def __rmul__( self, Other ): return      self.__ROperator__( Other, lambda A, B: A * B )
    def __rpow__( self, Other ): return      self.__ROperator__( Other, lambda A, B: A ** B )
    def __rmod__( self, Other ): return      self.__ROperator__( Other, lambda A, B: A % B )
    def __rtruediv__( self, Other ): return  self.__ROperator__( Other, lambda A, B: A / B )
    def __rfloordiv__( self, Other ): return self.__ROperator__( Other, lambda A, B: A // B )