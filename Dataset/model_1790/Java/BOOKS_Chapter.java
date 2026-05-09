





import java.util.List;
import java.util.ArrayList;

public class BOOKS_Chapter  {

    private int nbPages;
    private String title;



    public BOOKS_Chapter(
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


}