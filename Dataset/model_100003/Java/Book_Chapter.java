





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private String author;
    private String title;
    private String nbPages;



    public Book_Chapter(
        String author,        String title,        String nbPages    ) {
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
    public String getNbpages() {
        return nbPages;
    }

    public void setNbpages(String nbPages) {
        this.nbPages = nbPages;
    }


}