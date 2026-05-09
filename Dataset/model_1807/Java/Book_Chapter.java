





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private String nbPages;
    private String title;
    private String author;



    public Book_Chapter(
        String nbPages,        String title,        String author    ) {
        this.nbPages = nbPages;
        this.title = title;
        this.author = author;
    }


    public String getNbpages() {
        return nbPages;
    }

    public void setNbpages(String nbPages) {
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


}