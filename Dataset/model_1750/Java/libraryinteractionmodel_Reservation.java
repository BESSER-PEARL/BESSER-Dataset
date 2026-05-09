




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Reservation  {

    private LocalDate to;
    private LocalDate from_;





    private libraryinteractionmodel_Book libraryinteractionmodel_book;




    private libraryinteractionmodel_Book libraryinteractionmodel_book;


    public libraryinteractionmodel_Reservation(
        LocalDate to,        LocalDate from_    ) {
        this.to = to;
        this.from_ = from_;
    }


    public LocalDate getTo() {
        return to;
    }

    public void setTo(LocalDate to) {
        this.to = to;
    }
    public LocalDate getFrom_() {
        return from_;
    }

    public void setFrom_(LocalDate from_) {
        this.from_ = from_;
    }

    public libraryinteractionmodel_Book getLibraryinteractionmodel_book() {
        return libraryinteractionmodel_book;
    }

    public void setLibraryinteractionmodel_book(libraryinteractionmodel_Book libraryinteractionmodel_book) {
        this.libraryinteractionmodel_book = libraryinteractionmodel_book;
    }
    public libraryinteractionmodel_Book getLibraryinteractionmodel_book() {
        return libraryinteractionmodel_book;
    }

    public void setLibraryinteractionmodel_book(libraryinteractionmodel_Book libraryinteractionmodel_book) {
        this.libraryinteractionmodel_book = libraryinteractionmodel_book;
    }

}