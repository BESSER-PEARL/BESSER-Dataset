




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class library_BorrowedItem  {

    private LocalDate borrowDate;
    private LocalDate lastReturnDate;





    private library_Book library_book;




    private library_User library_user;




    private library_User library_user;


    public library_BorrowedItem(
        LocalDate borrowDate,        LocalDate lastReturnDate    ) {
        this.borrowDate = borrowDate;
        this.lastReturnDate = lastReturnDate;
    }


    public LocalDate getBorrowdate() {
        return borrowDate;
    }

    public void setBorrowdate(LocalDate borrowDate) {
        this.borrowDate = borrowDate;
    }
    public LocalDate getLastreturndate() {
        return lastReturnDate;
    }

    public void setLastreturndate(LocalDate lastReturnDate) {
        this.lastReturnDate = lastReturnDate;
    }

    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }
    public library_User getLibrary_user() {
        return library_user;
    }

    public void setLibrary_user(library_User library_user) {
        this.library_user = library_user;
    }
    public library_User getLibrary_user() {
        return library_user;
    }

    public void setLibrary_user(library_User library_user) {
        this.library_user = library_user;
    }

}