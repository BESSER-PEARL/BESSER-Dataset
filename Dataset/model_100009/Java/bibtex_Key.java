





import java.util.List;
import java.util.ArrayList;

public class bibtex_Key  {

    private String key;





    private bibtex_BibType bibtex_bibtype;


    public bibtex_Key(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public bibtex_BibType getBibtex_bibtype() {
        return bibtex_bibtype;
    }

    public void setBibtex_bibtype(bibtex_BibType bibtex_bibtype) {
        this.bibtex_bibtype = bibtex_bibtype;
    }

}