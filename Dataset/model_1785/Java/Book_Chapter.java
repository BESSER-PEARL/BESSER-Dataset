





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private int nbPages;
    private String title;





    private Book_Book book_book;


    public Book_Chapter(
        int nbPages,        String title    ) {
        this.nbPages = nbPages;
        this.title = title;
    }


    public int getNbpages() {
        return nbPages;
    }

    public void setNbpages(int nbPages) {
        this.nbPages = nbPages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(Book_Book book_book) {
        this.book_book = book_book;
    }

}