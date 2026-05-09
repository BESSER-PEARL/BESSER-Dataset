





import java.util.List;
import java.util.ArrayList;

public class bibTeX_CiteKey  {

    private String key;





    private bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes;


    public bibTeX_CiteKey(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public bibTeX_BibtexEntryTypes getBibtex_bibtexentrytypes() {
        return bibtex_bibtexentrytypes;
    }

    public void setBibtex_bibtexentrytypes(bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes) {
        this.bibtex_bibtexentrytypes = bibtex_bibtexentrytypes;
    }

}