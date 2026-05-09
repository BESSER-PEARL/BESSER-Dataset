





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private String author;
    private String title;
    private int nbPages;





    private Book_Book book_book;




    private Book_Book book_book;


    public Book_Chapter(
        String author,        String title,        int nbPages    ) {
        this.author = author;
        this.title = title;
        this.nbPages = nbPages;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getNbpages() {
        return nbPages;
    }

    public void setNbpages(int nbPages) {
        this.nbPages = nbPages;
    }

    public Book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(Book_Book book_book) {
        this.book_book = book_book;
    }
    public Book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(Book_Book book_book) {
        this.book_book = book_book;
    }

}