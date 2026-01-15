from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class comicBooks_Series:

    def __init__(self, seriesName: str, comicBooks_Series: "comicBooks_ComicBookCollection" = None, seriesPartOf: set["comicBooks_Book"] = None, Series: "comicBooks_Book" = None):
        self.seriesName = seriesName
        self.comicBooks_Series = comicBooks_Series
        self.seriesPartOf = seriesPartOf if seriesPartOf is not None else set()
        self.Series = Series
        
    @property
    def seriesName(self) -> str:
        return self.__seriesName

    @seriesName.setter
    def seriesName(self, seriesName: str):
        self.__seriesName = seriesName

    @property
    def comicBooks_Series(self):
        return self.__comicBooks_Series

    @comicBooks_Series.setter
    def comicBooks_Series(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Series__comicBooks_Series", None)
        self.__comicBooks_Series = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBooks_ComicBookCollection10"):
                opp_val = getattr(old_value, "comicBooks_ComicBookCollection10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBooks_ComicBookCollection10"):
                opp_val = getattr(value, "comicBooks_ComicBookCollection10", None)
                if opp_val is None:
                    setattr(value, "comicBooks_ComicBookCollection10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def seriesPartOf(self):
        return self.__seriesPartOf

    @seriesPartOf.setter
    def seriesPartOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Series__seriesPartOf", None)
        self.__seriesPartOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book13"):
                    opp_val = getattr(item, "Book13", None)
                    
                    if opp_val == self:
                        setattr(item, "Book13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book13"):
                    opp_val = getattr(item, "Book13", None)
                    
                    setattr(item, "Book13", self)
                    

    @property
    def Series(self):
        return self.__Series

    @Series.setter
    def Series(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Series__Series", None)
        self.__Series = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksInSeries"):
                opp_val = getattr(old_value, "booksInSeries", None)
                if opp_val == self:
                    setattr(old_value, "booksInSeries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksInSeries"):
                opp_val = getattr(value, "booksInSeries", None)
                setattr(value, "booksInSeries", self)

class comicBooks_Artist:

    def __init__(self, name: str, comicBooks_Artist: "comicBooks_ComicBookCollection" = None, Artist: "comicBooks_Book" = None, Artist18: "comicBooks_Book" = None, artists: set["comicBooks_Book"] = None, coverArtist: set["comicBooks_Book"] = None):
        self.name = name
        self.comicBooks_Artist = comicBooks_Artist
        self.Artist = Artist
        self.Artist18 = Artist18
        self.artists = artists if artists is not None else set()
        self.coverArtist = coverArtist if coverArtist is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Artist(self):
        return self.__Artist

    @Artist.setter
    def Artist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Artist__Artist", None)
        self.__Artist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksArtistFor"):
                opp_val = getattr(old_value, "booksArtistFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksArtistFor"):
                opp_val = getattr(value, "booksArtistFor", None)
                if opp_val is None:
                    setattr(value, "booksArtistFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Artist18(self):
        return self.__Artist18

    @Artist18.setter
    def Artist18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Artist__Artist18", None)
        self.__Artist18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksCoverArtistFor"):
                opp_val = getattr(old_value, "booksCoverArtistFor", None)
                if opp_val == self:
                    setattr(old_value, "booksCoverArtistFor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksCoverArtistFor"):
                opp_val = getattr(value, "booksCoverArtistFor", None)
                setattr(value, "booksCoverArtistFor", self)

    @property
    def comicBooks_Artist(self):
        return self.__comicBooks_Artist

    @comicBooks_Artist.setter
    def comicBooks_Artist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Artist__comicBooks_Artist", None)
        self.__comicBooks_Artist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBooks_ComicBookCollection2"):
                opp_val = getattr(old_value, "comicBooks_ComicBookCollection2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBooks_ComicBookCollection2"):
                opp_val = getattr(value, "comicBooks_ComicBookCollection2", None)
                if opp_val is None:
                    setattr(value, "comicBooks_ComicBookCollection2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def artists(self):
        return self.__artists

    @artists.setter
    def artists(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Artist__artists", None)
        self.__artists = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book22"):
                    opp_val = getattr(item, "Book22", None)
                    
                    if opp_val == self:
                        setattr(item, "Book22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book22"):
                    opp_val = getattr(item, "Book22", None)
                    
                    setattr(item, "Book22", self)
                    

    @property
    def coverArtist(self):
        return self.__coverArtist

    @coverArtist.setter
    def coverArtist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Artist__coverArtist", None)
        self.__coverArtist = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book24"):
                    opp_val = getattr(item, "Book24", None)
                    
                    if opp_val == self:
                        setattr(item, "Book24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book24"):
                    opp_val = getattr(item, "Book24", None)
                    
                    setattr(item, "Book24", self)
                    

class comicBooks_Publisher:

    def __init__(self, publishersName: str, comicBooks_Publisher: "comicBooks_ComicBookCollection" = None, publisher: set["comicBooks_Book"] = None, Publisher: "comicBooks_Book" = None):
        self.publishersName = publishersName
        self.comicBooks_Publisher = comicBooks_Publisher
        self.publisher = publisher if publisher is not None else set()
        self.Publisher = Publisher
        
    @property
    def publishersName(self) -> str:
        return self.__publishersName

    @publishersName.setter
    def publishersName(self, publishersName: str):
        self.__publishersName = publishersName

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Publisher__publisher", None)
        self.__publisher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def Publisher(self):
        return self.__Publisher

    @Publisher.setter
    def Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Publisher__Publisher", None)
        self.__Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksPublished"):
                opp_val = getattr(old_value, "booksPublished", None)
                if opp_val == self:
                    setattr(old_value, "booksPublished", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksPublished"):
                opp_val = getattr(value, "booksPublished", None)
                setattr(value, "booksPublished", self)

    @property
    def comicBooks_Publisher(self):
        return self.__comicBooks_Publisher

    @comicBooks_Publisher.setter
    def comicBooks_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Publisher__comicBooks_Publisher", None)
        self.__comicBooks_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBooks_ComicBookCollection8"):
                opp_val = getattr(old_value, "comicBooks_ComicBookCollection8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBooks_ComicBookCollection8"):
                opp_val = getattr(value, "comicBooks_ComicBookCollection8", None)
                if opp_val is None:
                    setattr(value, "comicBooks_ComicBookCollection8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comicBooks_Writer:

    def __init__(self, name: str, comicBooks_Writer: "comicBooks_ComicBookCollection" = None, Writer: "comicBooks_Book" = None, writers: set["comicBooks_Book"] = None):
        self.name = name
        self.comicBooks_Writer = comicBooks_Writer
        self.Writer = Writer
        self.writers = writers if writers is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksWriterFor"):
                opp_val = getattr(old_value, "booksWriterFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksWriterFor"):
                opp_val = getattr(value, "booksWriterFor", None)
                if opp_val is None:
                    setattr(value, "booksWriterFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def writers(self):
        return self.__writers

    @writers.setter
    def writers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Writer__writers", None)
        self.__writers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book28"):
                    opp_val = getattr(item, "Book28", None)
                    
                    if opp_val == self:
                        setattr(item, "Book28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book28"):
                    opp_val = getattr(item, "Book28", None)
                    
                    setattr(item, "Book28", self)
                    

    @property
    def comicBooks_Writer(self):
        return self.__comicBooks_Writer

    @comicBooks_Writer.setter
    def comicBooks_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Writer__comicBooks_Writer", None)
        self.__comicBooks_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBooks_ComicBookCollection6"):
                opp_val = getattr(old_value, "comicBooks_ComicBookCollection6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBooks_ComicBookCollection6"):
                opp_val = getattr(value, "comicBooks_ComicBookCollection6", None)
                if opp_val is None:
                    setattr(value, "comicBooks_ComicBookCollection6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comicBooks_Editor:

    def __init__(self, name: str, comicBooks_Editor: "comicBooks_ComicBookCollection" = None, Editor: "comicBooks_Book" = None, editors: set["comicBooks_Book"] = None):
        self.name = name
        self.comicBooks_Editor = comicBooks_Editor
        self.Editor = Editor
        self.editors = editors if editors is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comicBooks_Editor(self):
        return self.__comicBooks_Editor

    @comicBooks_Editor.setter
    def comicBooks_Editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Editor__comicBooks_Editor", None)
        self.__comicBooks_Editor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBooks_ComicBookCollection4"):
                opp_val = getattr(old_value, "comicBooks_ComicBookCollection4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBooks_ComicBookCollection4"):
                opp_val = getattr(value, "comicBooks_ComicBookCollection4", None)
                if opp_val is None:
                    setattr(value, "comicBooks_ComicBookCollection4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Editor(self):
        return self.__Editor

    @Editor.setter
    def Editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Editor__Editor", None)
        self.__Editor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booksEditorFor"):
                opp_val = getattr(old_value, "booksEditorFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booksEditorFor"):
                opp_val = getattr(value, "booksEditorFor", None)
                if opp_val is None:
                    setattr(value, "booksEditorFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editors(self):
        return self.__editors

    @editors.setter
    def editors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Editor__editors", None)
        self.__editors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book26"):
                    opp_val = getattr(item, "Book26", None)
                    
                    if opp_val == self:
                        setattr(item, "Book26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book26"):
                    opp_val = getattr(item, "Book26", None)
                    
                    setattr(item, "Book26", self)
                    

class comicBooks_Book:

    def __init__(self, name: str, publicationDate: str, comicBooks_Book: "comicBooks_ComicBookCollection" = None, Book: "comicBooks_Publisher" = None, booksArtistFor: set["comicBooks_Artist"] = None, Book13: "comicBooks_Series" = None, booksWriterFor: set["comicBooks_Writer"] = None, booksCoverArtistFor: "comicBooks_Artist" = None, booksPublished: "comicBooks_Publisher" = None, booksEditorFor: set["comicBooks_Editor"] = None, Book22: "comicBooks_Artist" = None, Book24: "comicBooks_Artist" = None, booksInSeries: "comicBooks_Series" = None, Book26: "comicBooks_Editor" = None, Book28: "comicBooks_Writer" = None):
        self.name = name
        self.publicationDate = publicationDate
        self.comicBooks_Book = comicBooks_Book
        self.Book = Book
        self.booksArtistFor = booksArtistFor if booksArtistFor is not None else set()
        self.Book13 = Book13
        self.booksWriterFor = booksWriterFor if booksWriterFor is not None else set()
        self.booksCoverArtistFor = booksCoverArtistFor
        self.booksPublished = booksPublished
        self.booksEditorFor = booksEditorFor if booksEditorFor is not None else set()
        self.Book22 = Book22
        self.Book24 = Book24
        self.booksInSeries = booksInSeries
        self.Book26 = Book26
        self.Book28 = Book28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def publicationDate(self) -> str:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: str):
        self.__publicationDate = publicationDate

    @property
    def booksArtistFor(self):
        return self.__booksArtistFor

    @booksArtistFor.setter
    def booksArtistFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__booksArtistFor", None)
        self.__booksArtistFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Artist"):
                    opp_val = getattr(item, "Artist", None)
                    
                    if opp_val == self:
                        setattr(item, "Artist", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Artist"):
                    opp_val = getattr(item, "Artist", None)
                    
                    setattr(item, "Artist", self)
                    

    @property
    def booksCoverArtistFor(self):
        return self.__booksCoverArtistFor

    @booksCoverArtistFor.setter
    def booksCoverArtistFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__booksCoverArtistFor", None)
        self.__booksCoverArtistFor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artist18"):
                opp_val = getattr(old_value, "Artist18", None)
                if opp_val == self:
                    setattr(old_value, "Artist18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artist18"):
                opp_val = getattr(value, "Artist18", None)
                setattr(value, "Artist18", self)

    @property
    def Book26(self):
        return self.__Book26

    @Book26.setter
    def Book26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__Book26", None)
        self.__Book26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editors"):
                opp_val = getattr(old_value, "editors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editors"):
                opp_val = getattr(value, "editors", None)
                if opp_val is None:
                    setattr(value, "editors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comicBooks_Book(self):
        return self.__comicBooks_Book

    @comicBooks_Book.setter
    def comicBooks_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__comicBooks_Book", None)
        self.__comicBooks_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comicBooks_ComicBookCollection"):
                opp_val = getattr(old_value, "comicBooks_ComicBookCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comicBooks_ComicBookCollection"):
                opp_val = getattr(value, "comicBooks_ComicBookCollection", None)
                if opp_val is None:
                    setattr(value, "comicBooks_ComicBookCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def booksInSeries(self):
        return self.__booksInSeries

    @booksInSeries.setter
    def booksInSeries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__booksInSeries", None)
        self.__booksInSeries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Series"):
                opp_val = getattr(old_value, "Series", None)
                if opp_val == self:
                    setattr(old_value, "Series", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Series"):
                opp_val = getattr(value, "Series", None)
                setattr(value, "Series", self)

    @property
    def Book22(self):
        return self.__Book22

    @Book22.setter
    def Book22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__Book22", None)
        self.__Book22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "artists"):
                opp_val = getattr(old_value, "artists", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "artists"):
                opp_val = getattr(value, "artists", None)
                if opp_val is None:
                    setattr(value, "artists", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book24(self):
        return self.__Book24

    @Book24.setter
    def Book24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__Book24", None)
        self.__Book24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coverArtist"):
                opp_val = getattr(old_value, "coverArtist", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coverArtist"):
                opp_val = getattr(value, "coverArtist", None)
                if opp_val is None:
                    setattr(value, "coverArtist", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book28(self):
        return self.__Book28

    @Book28.setter
    def Book28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__Book28", None)
        self.__Book28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers"):
                opp_val = getattr(old_value, "writers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers"):
                opp_val = getattr(value, "writers", None)
                if opp_val is None:
                    setattr(value, "writers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publisher"):
                opp_val = getattr(old_value, "publisher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publisher"):
                opp_val = getattr(value, "publisher", None)
                if opp_val is None:
                    setattr(value, "publisher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def booksEditorFor(self):
        return self.__booksEditorFor

    @booksEditorFor.setter
    def booksEditorFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__booksEditorFor", None)
        self.__booksEditorFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Editor"):
                    opp_val = getattr(item, "Editor", None)
                    
                    if opp_val == self:
                        setattr(item, "Editor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Editor"):
                    opp_val = getattr(item, "Editor", None)
                    
                    setattr(item, "Editor", self)
                    

    @property
    def booksPublished(self):
        return self.__booksPublished

    @booksPublished.setter
    def booksPublished(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__booksPublished", None)
        self.__booksPublished = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Publisher"):
                opp_val = getattr(old_value, "Publisher", None)
                if opp_val == self:
                    setattr(old_value, "Publisher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Publisher"):
                opp_val = getattr(value, "Publisher", None)
                setattr(value, "Publisher", self)

    @property
    def Book13(self):
        return self.__Book13

    @Book13.setter
    def Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__Book13", None)
        self.__Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seriesPartOf"):
                opp_val = getattr(old_value, "seriesPartOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seriesPartOf"):
                opp_val = getattr(value, "seriesPartOf", None)
                if opp_val is None:
                    setattr(value, "seriesPartOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def booksWriterFor(self):
        return self.__booksWriterFor

    @booksWriterFor.setter
    def booksWriterFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comicBooks_Book__booksWriterFor", None)
        self.__booksWriterFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    setattr(item, "Writer", self)
                    

class comicBooks_ComicBookCollection:

    pass