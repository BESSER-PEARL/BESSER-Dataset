





import java.util.List;
import java.util.ArrayList;

public class bibTeX_BibTeXEntry  {

    private String theId;





    private bibTeX_BibTeXFile bibtex_bibtexfile;


    public bibTeX_BibTeXEntry(
        String theId    ) {
        this.theId = theId;
    }


    public String getTheid() {
        return theId;
    }

    public void setTheid(String theId) {
        this.theId = theId;
    }

    public bibTeX_BibTeXFile getBibtex_bibtexfile() {
        return bibtex_bibtexfile;
    }

    public void setBibtex_bibtexfile(bibTeX_BibTeXFile bibtex_bibtexfile) {
        this.bibtex_bibtexfile = bibtex_bibtexfile;
    }

}