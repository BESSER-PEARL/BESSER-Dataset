





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private int nbPages;
    private String title;
    private String author;



    public Book_Chapter(
        int nbPages,        String title,        String author    ) {
        this.nbPages = nbPages;
        this.title = title;
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
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}