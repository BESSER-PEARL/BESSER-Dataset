from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class spreadsheet_Header:

    pass
class spreadsheet_Row:

    pass
class spreadsheet_Point:

    def __init__(self, x: int, y: int, spreadsheet_Point: "spreadsheet_Image" = None, spreadsheet_Point23: "spreadsheet_Table" = None, spreadsheet_Point28: "spreadsheet_Cell" = None):
        self.x = x
        self.y = y
        self.spreadsheet_Point = spreadsheet_Point
        self.spreadsheet_Point23 = spreadsheet_Point23
        self.spreadsheet_Point28 = spreadsheet_Point28
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def spreadsheet_Point(self):
        return self.__spreadsheet_Point

    @spreadsheet_Point.setter
    def spreadsheet_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Point__spreadsheet_Point", None)
        self.__spreadsheet_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Image13"):
                opp_val = getattr(old_value, "spreadsheet_Image13", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Image13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Image13"):
                opp_val = getattr(value, "spreadsheet_Image13", None)
                setattr(value, "spreadsheet_Image13", self)

    @property
    def spreadsheet_Point28(self):
        return self.__spreadsheet_Point28

    @spreadsheet_Point28.setter
    def spreadsheet_Point28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Point__spreadsheet_Point28", None)
        self.__spreadsheet_Point28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Cell27"):
                opp_val = getattr(old_value, "spreadsheet_Cell27", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Cell27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Cell27"):
                opp_val = getattr(value, "spreadsheet_Cell27", None)
                setattr(value, "spreadsheet_Cell27", self)

    @property
    def spreadsheet_Point23(self):
        return self.__spreadsheet_Point23

    @spreadsheet_Point23.setter
    def spreadsheet_Point23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Point__spreadsheet_Point23", None)
        self.__spreadsheet_Point23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Table22"):
                opp_val = getattr(old_value, "spreadsheet_Table22", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Table22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Table22"):
                opp_val = getattr(value, "spreadsheet_Table22", None)
                setattr(value, "spreadsheet_Table22", self)

class ContentElement:

    pass
class spreadsheet_Cell(ContentElement):

    def __init__(self, spreadsheet_Cell: "spreadsheet_Header" = None, spreadsheet_Cell31: "spreadsheet_Row" = None, spreadsheet_Cell27: "spreadsheet_Point" = None):
        self.spreadsheet_Cell = spreadsheet_Cell
        self.spreadsheet_Cell31 = spreadsheet_Cell31
        self.spreadsheet_Cell27 = spreadsheet_Cell27
        
        pass
    @property
    def spreadsheet_Cell27(self):
        return self.__spreadsheet_Cell27

    @spreadsheet_Cell27.setter
    def spreadsheet_Cell27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__spreadsheet_Cell27", None)
        self.__spreadsheet_Cell27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Point28"):
                opp_val = getattr(old_value, "spreadsheet_Point28", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Point28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Point28"):
                opp_val = getattr(value, "spreadsheet_Point28", None)
                setattr(value, "spreadsheet_Point28", self)

    @property
    def spreadsheet_Cell(self):
        return self.__spreadsheet_Cell

    @spreadsheet_Cell.setter
    def spreadsheet_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__spreadsheet_Cell", None)
        self.__spreadsheet_Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Header25"):
                opp_val = getattr(old_value, "spreadsheet_Header25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Header25"):
                opp_val = getattr(value, "spreadsheet_Header25", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_Header25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spreadsheet_Cell31(self):
        return self.__spreadsheet_Cell31

    @spreadsheet_Cell31.setter
    def spreadsheet_Cell31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__spreadsheet_Cell31", None)
        self.__spreadsheet_Cell31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Row30"):
                opp_val = getattr(old_value, "spreadsheet_Row30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Row30"):
                opp_val = getattr(value, "spreadsheet_Row30", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_Row30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getRowNumber(self) :
        # TODO: Implement getRowNumber method
        pass

    def getColNumber(self) :
        # TODO: Implement getColNumber method
        pass

    def offset(self, spreadsheet_x, spreadsheet_y) :
        # TODO: Implement offset method
        pass

class spreadsheet_Title(ContentElement):

    def __init__(self, hiearchy: str, spreadsheet_Title: "spreadsheet_Text" = None, spreadsheet_Title11: "spreadsheet_Image" = None, spreadsheet_Title16: "spreadsheet_Table" = None):
        self.hiearchy = hiearchy
        self.spreadsheet_Title = spreadsheet_Title
        self.spreadsheet_Title11 = spreadsheet_Title11
        self.spreadsheet_Title16 = spreadsheet_Title16
        
        pass
    @property
    def hiearchy(self):
        return self.__hiearchy

    @hiearchy.setter
    def hiearchy(self, hiearchy: str):
        self.__hiearchy = hiearchy


    @property
    def spreadsheet_Title11(self):
        return self.__spreadsheet_Title11

    @spreadsheet_Title11.setter
    def spreadsheet_Title11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Title__spreadsheet_Title11", None)
        self.__spreadsheet_Title11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Image10"):
                opp_val = getattr(old_value, "spreadsheet_Image10", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Image10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Image10"):
                opp_val = getattr(value, "spreadsheet_Image10", None)
                setattr(value, "spreadsheet_Image10", self)

    @property
    def spreadsheet_Title16(self):
        return self.__spreadsheet_Title16

    @spreadsheet_Title16.setter
    def spreadsheet_Title16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Title__spreadsheet_Title16", None)
        self.__spreadsheet_Title16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Table15"):
                opp_val = getattr(old_value, "spreadsheet_Table15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Table15"):
                opp_val = getattr(value, "spreadsheet_Table15", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_Table15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spreadsheet_Title(self):
        return self.__spreadsheet_Title

    @spreadsheet_Title.setter
    def spreadsheet_Title(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Title__spreadsheet_Title", None)
        self.__spreadsheet_Title = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Text8"):
                opp_val = getattr(old_value, "spreadsheet_Text8", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Text8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Text8"):
                opp_val = getattr(value, "spreadsheet_Text8", None)
                setattr(value, "spreadsheet_Text8", self)

class spreadsheet_Text:

    def __init__(self, textContent: str, spreadsheet_Text8: "spreadsheet_Title" = None, spreadsheet_Text: "spreadsheet_Sheet" = None):
        self.textContent = textContent
        self.spreadsheet_Text8 = spreadsheet_Text8
        self.spreadsheet_Text = spreadsheet_Text
        
        pass
    @property
    def textContent(self):
        return self.__textContent

    @textContent.setter
    def textContent(self, textContent: str):
        self.__textContent = textContent


    @property
    def spreadsheet_Text(self):
        return self.__spreadsheet_Text

    @spreadsheet_Text.setter
    def spreadsheet_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Text__spreadsheet_Text", None)
        self.__spreadsheet_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Sheet2"):
                opp_val = getattr(old_value, "spreadsheet_Sheet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Sheet2"):
                opp_val = getattr(value, "spreadsheet_Sheet2", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_Sheet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spreadsheet_Text8(self):
        return self.__spreadsheet_Text8

    @spreadsheet_Text8.setter
    def spreadsheet_Text8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Text__spreadsheet_Text8", None)
        self.__spreadsheet_Text8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Title"):
                opp_val = getattr(old_value, "spreadsheet_Title", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Title", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Title"):
                opp_val = getattr(value, "spreadsheet_Title", None)
                setattr(value, "spreadsheet_Title", self)

class spreadsheet_Sheet:

    def __init__(self, name: str, spreadsheet_Sheet4: set["spreadsheet_Image"] = None, spreadsheet_Sheet6: set["spreadsheet_Table"] = None, spreadsheet_Sheet: "spreadsheet_SpreadsheetFile" = None, spreadsheet_Sheet2: set["spreadsheet_Text"] = None):
        self.name = name
        self.spreadsheet_Sheet4 = spreadsheet_Sheet4 if spreadsheet_Sheet4 is not None else set()
        self.spreadsheet_Sheet6 = spreadsheet_Sheet6 if spreadsheet_Sheet6 is not None else set()
        self.spreadsheet_Sheet = spreadsheet_Sheet
        self.spreadsheet_Sheet2 = spreadsheet_Sheet2 if spreadsheet_Sheet2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def spreadsheet_Sheet6(self):
        return self.__spreadsheet_Sheet6

    @spreadsheet_Sheet6.setter
    def spreadsheet_Sheet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__spreadsheet_Sheet6", None)
        self.__spreadsheet_Sheet6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Table"):
                    opp_val = getattr(item, "spreadsheet_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Table"):
                    opp_val = getattr(item, "spreadsheet_Table", None)
                    
                    setattr(item, "spreadsheet_Table", self)
                    

    @property
    def spreadsheet_Sheet4(self):
        return self.__spreadsheet_Sheet4

    @spreadsheet_Sheet4.setter
    def spreadsheet_Sheet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__spreadsheet_Sheet4", None)
        self.__spreadsheet_Sheet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Image"):
                    opp_val = getattr(item, "spreadsheet_Image", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Image", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Image"):
                    opp_val = getattr(item, "spreadsheet_Image", None)
                    
                    setattr(item, "spreadsheet_Image", self)
                    

    @property
    def spreadsheet_Sheet2(self):
        return self.__spreadsheet_Sheet2

    @spreadsheet_Sheet2.setter
    def spreadsheet_Sheet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__spreadsheet_Sheet2", None)
        self.__spreadsheet_Sheet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Text"):
                    opp_val = getattr(item, "spreadsheet_Text", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Text", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Text"):
                    opp_val = getattr(item, "spreadsheet_Text", None)
                    
                    setattr(item, "spreadsheet_Text", self)
                    

    @property
    def spreadsheet_Sheet(self):
        return self.__spreadsheet_Sheet

    @spreadsheet_Sheet.setter
    def spreadsheet_Sheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__spreadsheet_Sheet", None)
        self.__spreadsheet_Sheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_SpreadsheetFile"):
                opp_val = getattr(old_value, "spreadsheet_SpreadsheetFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_SpreadsheetFile"):
                opp_val = getattr(value, "spreadsheet_SpreadsheetFile", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_SpreadsheetFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DocumentModel:

    pass
class spreadsheet_SpreadsheetFile(DocumentModel):

    def __init__(self, nbSheet: int, spreadsheet_SpreadsheetFile: set["spreadsheet_Sheet"] = None):
        self.nbSheet = nbSheet
        self.spreadsheet_SpreadsheetFile = spreadsheet_SpreadsheetFile if spreadsheet_SpreadsheetFile is not None else set()
        
        pass
    @property
    def nbSheet(self):
        return self.__nbSheet

    @nbSheet.setter
    def nbSheet(self, nbSheet: int):
        self.__nbSheet = nbSheet


    @property
    def spreadsheet_SpreadsheetFile(self):
        return self.__spreadsheet_SpreadsheetFile

    @spreadsheet_SpreadsheetFile.setter
    def spreadsheet_SpreadsheetFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_SpreadsheetFile__spreadsheet_SpreadsheetFile", None)
        self.__spreadsheet_SpreadsheetFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Sheet"):
                    opp_val = getattr(item, "spreadsheet_Sheet", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Sheet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Sheet"):
                    opp_val = getattr(item, "spreadsheet_Sheet", None)
                    
                    setattr(item, "spreadsheet_Sheet", self)
                    

class spreadsheet_Table:

    def __init__(self, nbColumns: int, spreadsheet_Table15: set["spreadsheet_Title"] = None, spreadsheet_Table20: set["spreadsheet_Row"] = None, spreadsheet_Table22: "spreadsheet_Point" = None, spreadsheet_Table18: set["spreadsheet_Header"] = None, spreadsheet_Table: "spreadsheet_Sheet" = None):
        self.nbColumns = nbColumns
        self.spreadsheet_Table15 = spreadsheet_Table15 if spreadsheet_Table15 is not None else set()
        self.spreadsheet_Table20 = spreadsheet_Table20 if spreadsheet_Table20 is not None else set()
        self.spreadsheet_Table22 = spreadsheet_Table22
        self.spreadsheet_Table18 = spreadsheet_Table18 if spreadsheet_Table18 is not None else set()
        self.spreadsheet_Table = spreadsheet_Table
        
        pass
    @property
    def nbColumns(self):
        return self.__nbColumns

    @nbColumns.setter
    def nbColumns(self, nbColumns: int):
        self.__nbColumns = nbColumns


    @property
    def spreadsheet_Table22(self):
        return self.__spreadsheet_Table22

    @spreadsheet_Table22.setter
    def spreadsheet_Table22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Table__spreadsheet_Table22", None)
        self.__spreadsheet_Table22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Point23"):
                opp_val = getattr(old_value, "spreadsheet_Point23", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Point23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Point23"):
                opp_val = getattr(value, "spreadsheet_Point23", None)
                setattr(value, "spreadsheet_Point23", self)

    @property
    def spreadsheet_Table18(self):
        return self.__spreadsheet_Table18

    @spreadsheet_Table18.setter
    def spreadsheet_Table18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Table__spreadsheet_Table18", None)
        self.__spreadsheet_Table18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Header"):
                    opp_val = getattr(item, "spreadsheet_Header", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Header", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Header"):
                    opp_val = getattr(item, "spreadsheet_Header", None)
                    
                    setattr(item, "spreadsheet_Header", self)
                    

    @property
    def spreadsheet_Table15(self):
        return self.__spreadsheet_Table15

    @spreadsheet_Table15.setter
    def spreadsheet_Table15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Table__spreadsheet_Table15", None)
        self.__spreadsheet_Table15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Title16"):
                    opp_val = getattr(item, "spreadsheet_Title16", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Title16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Title16"):
                    opp_val = getattr(item, "spreadsheet_Title16", None)
                    
                    setattr(item, "spreadsheet_Title16", self)
                    

    @property
    def spreadsheet_Table20(self):
        return self.__spreadsheet_Table20

    @spreadsheet_Table20.setter
    def spreadsheet_Table20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Table__spreadsheet_Table20", None)
        self.__spreadsheet_Table20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spreadsheet_Row"):
                    opp_val = getattr(item, "spreadsheet_Row", None)
                    
                    if opp_val == self:
                        setattr(item, "spreadsheet_Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spreadsheet_Row"):
                    opp_val = getattr(item, "spreadsheet_Row", None)
                    
                    setattr(item, "spreadsheet_Row", self)
                    

    @property
    def spreadsheet_Table(self):
        return self.__spreadsheet_Table

    @spreadsheet_Table.setter
    def spreadsheet_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Table__spreadsheet_Table", None)
        self.__spreadsheet_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Sheet6"):
                opp_val = getattr(old_value, "spreadsheet_Sheet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Sheet6"):
                opp_val = getattr(value, "spreadsheet_Sheet6", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_Sheet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spreadsheet_Image:

    def __init__(self, width: int, height: int, spreadsheet_Image10: "spreadsheet_Title" = None, spreadsheet_Image13: "spreadsheet_Point" = None, spreadsheet_Image: "spreadsheet_Sheet" = None):
        self.width = width
        self.height = height
        self.spreadsheet_Image10 = spreadsheet_Image10
        self.spreadsheet_Image13 = spreadsheet_Image13
        self.spreadsheet_Image = spreadsheet_Image
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def spreadsheet_Image(self):
        return self.__spreadsheet_Image

    @spreadsheet_Image.setter
    def spreadsheet_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Image__spreadsheet_Image", None)
        self.__spreadsheet_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Sheet4"):
                opp_val = getattr(old_value, "spreadsheet_Sheet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Sheet4"):
                opp_val = getattr(value, "spreadsheet_Sheet4", None)
                if opp_val is None:
                    setattr(value, "spreadsheet_Sheet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def spreadsheet_Image13(self):
        return self.__spreadsheet_Image13

    @spreadsheet_Image13.setter
    def spreadsheet_Image13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Image__spreadsheet_Image13", None)
        self.__spreadsheet_Image13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Point"):
                opp_val = getattr(old_value, "spreadsheet_Point", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Point"):
                opp_val = getattr(value, "spreadsheet_Point", None)
                setattr(value, "spreadsheet_Point", self)

    @property
    def spreadsheet_Image10(self):
        return self.__spreadsheet_Image10

    @spreadsheet_Image10.setter
    def spreadsheet_Image10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Image__spreadsheet_Image10", None)
        self.__spreadsheet_Image10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spreadsheet_Title11"):
                opp_val = getattr(old_value, "spreadsheet_Title11", None)
                if opp_val == self:
                    setattr(old_value, "spreadsheet_Title11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spreadsheet_Title11"):
                opp_val = getattr(value, "spreadsheet_Title11", None)
                setattr(value, "spreadsheet_Title11", self)
