





import java.util.List;
import java.util.ArrayList;

public class BibTeX_BibTeXEntry  {

    private String id;





    private BibTeX_BibTeXFile bibtex_bibtexfile;


    public BibTeX_BibTeXEntry(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public BibTeX_BibTeXFile getBibtex_bibtexfile() {
        return bibtex_bibtexfile;
    }

    public void setBibtex_bibtexfile(BibTeX_BibTeXFile bibtex_bibtexfile) {
        this.bibtex_bibtexfile = bibtex_bibtexfile;
    }

}