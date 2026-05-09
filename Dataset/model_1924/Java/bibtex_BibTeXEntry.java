





import java.util.List;
import java.util.ArrayList;

public class bibtex_BibTeXEntry  {

    private String id;





    private bibtex_BibTeXFile bibtex_bibtexfile;


    public bibtex_BibTeXEntry(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bibtex_BibTeXFile getBibtex_bibtexfile() {
        return bibtex_bibtexfile;
    }

    public void setBibtex_bibtexfile(bibtex_BibTeXFile bibtex_bibtexfile) {
        this.bibtex_bibtexfile = bibtex_bibtexfile;
    }

}