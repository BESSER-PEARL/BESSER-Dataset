





import java.util.List;
import java.util.ArrayList;

public class bookstore_Book extends Ent {

    private String title;
    private int pages;





    private bookstore_Person bookstore_person;




    private bookstore_Book bookstore_book;




    private bookstore_Dvd bookstore_dvd;


    public bookstore_Book(
        String title,        int pages    ) {
        super(
        );
        this.title = title;
        this.pages = pages;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public bookstore_Person getBookstore_person() {
        return bookstore_person;
    }

    public void setBookstore_person(bookstore_Person bookstore_person) {
        this.bookstore_person = bookstore_person;
    }
    public bookstore_Book getBookstore_book() {
        return bookstore_book;
    }

    public void setBookstore_book(bookstore_Book bookstore_book) {
        this.bookstore_book = bookstore_book;
    }
    public bookstore_Dvd getBookstore_dvd() {
        return bookstore_dvd;
    }

    public void setBookstore_dvd(bookstore_Dvd bookstore_dvd) {
        this.bookstore_dvd = bookstore_dvd;
    }

}