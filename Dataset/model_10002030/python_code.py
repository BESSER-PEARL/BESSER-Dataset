from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class patronrecord:

    def __init__(self, patronid: str, type: str, dateofmembership: str, noofbooks_alooted: str, name: str, phone_no: str, address: str, filesowned: str, patron7: "patron" = None):
        self.patronid = patronid
        self.type = type
        self.dateofmembership = dateofmembership
        self.noofbooks_alooted = noofbooks_alooted
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.filesowned = filesowned
        self.patron7 = patron7
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def noofbooks_alooted(self):
        return self.__noofbooks_alooted
    @noofbooks_alooted.setter
    def noofbooks_alooted(self, noofbooks_alooted: str):
        self.__noofbooks_alooted = noofbooks_alooted

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def patronid(self):
        return self.__patronid
    @patronid.setter
    def patronid(self, patronid: str):
        self.__patronid = patronid

    @property
    def dateofmembership(self):
        return self.__dateofmembership
    @dateofmembership.setter
    def dateofmembership(self, dateofmembership: str):
        self.__dateofmembership = dateofmembership

    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: str):
        self.__phone_no = phone_no

    @property
    def filesowned(self):
        return self.__filesowned
    @filesowned.setter
    def filesowned(self, filesowned: str):
        self.__filesowned = filesowned

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patron7(self):
        return self.__patron7
    @patron7.setter
    def patron7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patronrecord__patron7", None)
        self.__patron7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patronrecord6"):
                opp_val = getattr(old_value, "patronrecord6", None)
                if opp_val == self:
                    setattr(old_value, "patronrecord6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patronrecord6"):
                opp_val = getattr(value, "patronrecord6", None)
                setattr(value, "patronrecord6", self)



class vendor:

    def __init__(self, search: str, supplybooks: str, bookdetails: str, paymentdetails: str):
        self.search = search
        self.supplybooks = supplybooks
        self.bookdetails = bookdetails
        self.paymentdetails = paymentdetails
        
        pass
    @property
    def bookdetails(self):
        return self.__bookdetails
    @bookdetails.setter
    def bookdetails(self, bookdetails: str):
        self.__bookdetails = bookdetails

    @property
    def paymentdetails(self):
        return self.__paymentdetails
    @paymentdetails.setter
    def paymentdetails(self, paymentdetails: str):
        self.__paymentdetails = paymentdetails

    @property
    def supplybooks(self):
        return self.__supplybooks
    @supplybooks.setter
    def supplybooks(self, supplybooks: str):
        self.__supplybooks = supplybooks

    @property
    def search(self):
        return self.__search
    @search.setter
    def search(self, search: str):
        self.__search = search



class patron:

    def __init__(self, details: str, patronid: str, search: str, request: str, payfine: str, book_mdatabase5: "book_mdatabase" = None, patronrecord6: "patronrecord" = None):
        self.details = details
        self.patronid = patronid
        self.search = search
        self.request = request
        self.payfine = payfine
        self.book_mdatabase5 = book_mdatabase5
        self.patronrecord6 = patronrecord6
        
        pass
    @property
    def request(self):
        return self.__request
    @request.setter
    def request(self, request: str):
        self.__request = request

    @property
    def search(self):
        return self.__search
    @search.setter
    def search(self, search: str):
        self.__search = search

    @property
    def payfine(self):
        return self.__payfine
    @payfine.setter
    def payfine(self, payfine: str):
        self.__payfine = payfine

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def patronid(self):
        return self.__patronid
    @patronid.setter
    def patronid(self, patronid: str):
        self.__patronid = patronid

    @property
    def patronrecord6(self):
        return self.__patronrecord6
    @patronrecord6.setter
    def patronrecord6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patron__patronrecord6", None)
        self.__patronrecord6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron7"):
                opp_val = getattr(old_value, "patron7", None)
                if opp_val == self:
                    setattr(old_value, "patron7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron7"):
                opp_val = getattr(value, "patron7", None)
                setattr(value, "patron7", self)

    @property
    def book_mdatabase5(self):
        return self.__book_mdatabase5
    @book_mdatabase5.setter
    def book_mdatabase5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patron__book_mdatabase5", None)
        self.__book_mdatabase5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patron4"):
                opp_val = getattr(old_value, "patron4", None)
                if opp_val == self:
                    setattr(old_value, "patron4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patron4"):
                opp_val = getattr(value, "patron4", None)
                setattr(value, "patron4", self)



class book_mdatabase:

    def __init__(self, booktitle: str, author: str, bookid: str, update: str, library3: "library" = None, patron4: "patron" = None):
        self.booktitle = booktitle
        self.author = author
        self.bookid = bookid
        self.update = update
        self.library3 = library3
        self.patron4 = patron4
        
        pass
    @property
    def update(self):
        return self.__update
    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def booktitle(self):
        return self.__booktitle
    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

    @property
    def bookid(self):
        return self.__bookid
    @bookid.setter
    def bookid(self, bookid: str):
        self.__bookid = bookid

    @property
    def library3(self):
        return self.__library3
    @library3.setter
    def library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_mdatabase__library3", None)
        self.__library3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_mdatabase2"):
                opp_val = getattr(old_value, "book_mdatabase2", None)
                if opp_val == self:
                    setattr(old_value, "book_mdatabase2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_mdatabase2"):
                opp_val = getattr(value, "book_mdatabase2", None)
                setattr(value, "book_mdatabase2", self)

    @property
    def patron4(self):
        return self.__patron4
    @patron4.setter
    def patron4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_mdatabase__patron4", None)
        self.__patron4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_mdatabase5"):
                opp_val = getattr(old_value, "book_mdatabase5", None)
                if opp_val == self:
                    setattr(old_value, "book_mdatabase5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_mdatabase5"):
                opp_val = getattr(value, "book_mdatabase5", None)
                setattr(value, "book_mdatabase5", self)



class LIBRARIAN:

    def __init__(self, NAME: str, LIBRARIAN_ID: str, issue_status: str, searchbook__: str, issue_book: str, verify_member__: str, library1: "library" = None):
        self.NAME = NAME
        self.LIBRARIAN_ID = LIBRARIAN_ID
        self.issue_status = issue_status
        self.searchbook__ = searchbook__
        self.issue_book = issue_book
        self.verify_member__ = verify_member__
        self.library1 = library1
        
        pass
    @property
    def NAME(self):
        return self.__NAME
    @NAME.setter
    def NAME(self, NAME: str):
        self.__NAME = NAME

    @property
    def LIBRARIAN_ID(self):
        return self.__LIBRARIAN_ID
    @LIBRARIAN_ID.setter
    def LIBRARIAN_ID(self, LIBRARIAN_ID: str):
        self.__LIBRARIAN_ID = LIBRARIAN_ID

    @property
    def verify_member__(self):
        return self.__verify_member__
    @verify_member__.setter
    def verify_member__(self, verify_member__: str):
        self.__verify_member__ = verify_member__

    @property
    def searchbook__(self):
        return self.__searchbook__
    @searchbook__.setter
    def searchbook__(self, searchbook__: str):
        self.__searchbook__ = searchbook__

    @property
    def issue_book(self):
        return self.__issue_book
    @issue_book.setter
    def issue_book(self, issue_book: str):
        self.__issue_book = issue_book

    @property
    def issue_status(self):
        return self.__issue_status
    @issue_status.setter
    def issue_status(self, issue_status: str):
        self.__issue_status = issue_status

    @property
    def library1(self):
        return self.__library1
    @library1.setter
    def library1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LIBRARIAN__library1", None)
        self.__library1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lIBRARIAN0"):
                opp_val = getattr(old_value, "lIBRARIAN0", None)
                if opp_val == self:
                    setattr(old_value, "lIBRARIAN0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lIBRARIAN0"):
                opp_val = getattr(value, "lIBRARIAN0", None)
                setattr(value, "lIBRARIAN0", self)



class library:

    def __init__(self, _location: str, _librarion_id: str, lIBRARIAN0: "LIBRARIAN" = None, book_mdatabase2: "book_mdatabase" = None):
        self._location = _location
        self._librarion_id = _librarion_id
        self.lIBRARIAN0 = lIBRARIAN0
        self.book_mdatabase2 = book_mdatabase2
        
        pass
    @property
    def _librarion_id(self):
        return self.___librarion_id
    @_librarion_id.setter
    def _librarion_id(self, _librarion_id: str):
        self.___librarion_id = _librarion_id

    @property
    def _location(self):
        return self.___location
    @_location.setter
    def _location(self, _location: str):
        self.___location = _location

    @property
    def lIBRARIAN0(self):
        return self.__lIBRARIAN0
    @lIBRARIAN0.setter
    def lIBRARIAN0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library__lIBRARIAN0", None)
        self.__lIBRARIAN0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library1"):
                opp_val = getattr(old_value, "library1", None)
                if opp_val == self:
                    setattr(old_value, "library1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library1"):
                opp_val = getattr(value, "library1", None)
                setattr(value, "library1", self)

    @property
    def book_mdatabase2(self):
        return self.__book_mdatabase2
    @book_mdatabase2.setter
    def book_mdatabase2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library__book_mdatabase2", None)
        self.__book_mdatabase2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3"):
                opp_val = getattr(old_value, "library3", None)
                if opp_val == self:
                    setattr(old_value, "library3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3"):
                opp_val = getattr(value, "library3", None)
                setattr(value, "library3", self)

