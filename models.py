from sqlalchemy import Column, Integer, Text
from database import Base
from flask.ext.login import UserMixin

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Alter = Column(Text, nullable=False, unique=True)
    Geschlecht = Column(Text, nullable=True)
    Bildung = Column(Text, nullable=True)
    Instrument = Column(Integer, nullable=True)
    Aktiv = Column(Integer, nullable=True)
    Passiv = Column(Integer, nullable=True)
    Konzerte = Column(Integer, nullable=True)
    Information = Column(Integer, nullable=True)
    Tagging = Column(Text, nullable=True)
    BandViel1 = Column(Text, nullable=True)
    BandViel2 = Column(Text, nullable=True)
    BandViel3 = Column(Text, nullable=True)
    BandMittel1 = Column(Text, nullable=True)
    BandMittel2 = Column(Text, nullable=True)
    BandMittel3 = Column(Text, nullable=True)
    BandWenig1 = Column(Text, nullable=True)
    BandWenig2 = Column(Text, nullable=True)
    BandWenig3 = Column(Text, nullable=True)
    


    def __init__(self, Alter=None, Geschlecht=None, Bildung=None, Instrument=None, Aktiv=None, Passiv=None, Konzerte=None, Information=None, Tagging=None,
                 BandViel1=None, BandViel2=None, BandViel3=None, BandMittel1=None, BandMittel2=None, BandMittel3=None, BandWenig1=None, BandWenig2=None, BandWenig3=None):
        self.Alter = Alter
        self.Geschlecht = Geschlecht
        self.Bildung = Bildung
        self.Instrument = Instrument
        self.Aktiv = Aktiv
        self.Passiv = Passiv
        self.Konzerte = Konzerte
        self.Information = Information
        self.Tagging = Tagging
        self.BandViel1 = BandViel1
        self.BandViel2 = BandViel2
        self.BandViel3 = BandViel3
        self.BandMittel1 = BandMittel1
        self.BandMittel2 = BandMittel2
        self.BandMittel3 = BandMittel3
        self.BandWenig1 = BandWenig1
        self.BandWenig2 = BandWenig2
        self.BandWenig3 = BandWenig3
        
        

    def get(self, id):
        if self.id == id:
            return self
        else:
            return None


    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id, self.username)