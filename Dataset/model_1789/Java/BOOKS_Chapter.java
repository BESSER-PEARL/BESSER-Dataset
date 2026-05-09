





import java.util.List;
import java.util.ArrayList;

public class BOOKS_Chapter  {

    private String title;
    private int nbPages;



    public BOOKS_Chapter(
        String title,        int nbPages    ) {
        this.title = title;
        this.nbPages = nbPages;
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


}