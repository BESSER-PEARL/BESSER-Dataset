





import java.util.List;
import java.util.ArrayList;

public class Publication_Publication  {

    private String nbPages;
    private String title;
    private String authors;



    public Publication_Publication(
        String nbPages,        String title,        String authors    ) {
        this.nbPages = nbPages;
        this.title = title;
        this.authors = authors;
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
    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }


}