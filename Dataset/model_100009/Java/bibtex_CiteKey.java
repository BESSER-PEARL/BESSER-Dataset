





import java.util.List;
import java.util.ArrayList;

public class bibtex_CiteKey  {

    private String citeKey;





    private bibtex_BibType bibtex_bibtype;


    public bibtex_CiteKey(
        String citeKey    ) {
        this.citeKey = citeKey;
    }


    public String getCitekey() {
        return citeKey;
    }

    public void setCitekey(String citeKey) {
        this.citeKey = citeKey;
    }

    public bibtex_BibType getBibtex_bibtype() {
        return bibtex_bibtype;
    }

    public void setBibtex_bibtype(bibtex_BibType bibtex_bibtype) {
        this.bibtex_bibtype = bibtex_bibtype;
    }

}