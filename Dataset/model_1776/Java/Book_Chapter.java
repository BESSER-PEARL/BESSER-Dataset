





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private String title;
    private String author;
    private int nbPages;





    private Book book;


    public Book_Chapter(
        String title,        String author,        int nbPages    ) {
        this.title = title;
        this.author = author;
        this.nbPages = nbPages;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
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

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }

}