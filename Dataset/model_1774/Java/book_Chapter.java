





import java.util.List;
import java.util.ArrayList;

public class book_Chapter  {

    private String author;
    private int nbPages;
    private String title;





    private book_Book book_book;




    private book_Book book_book;


    public book_Chapter(
        String author,        int nbPages,        String title    ) {
        this.author = author;
        this.nbPages = nbPages;
        this.title = title;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
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

    public book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(book_Book book_book) {
        this.book_book = book_book;
    }
    public book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(book_Book book_book) {
        this.book_book = book_book;
    }

}