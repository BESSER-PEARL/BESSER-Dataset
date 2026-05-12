





import java.util.List;
import java.util.ArrayList;

public class bibtex_Title  {

    private String title;





    private bibtex_BibType bibtex_bibtype;


    public bibtex_Title(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bibtex_BibType getBibtex_bibtype() {
        return bibtex_bibtype;
    }

    public void setBibtex_bibtype(bibtex_BibType bibtex_bibtype) {
        this.bibtex_bibtype = bibtex_bibtype;
    }

}