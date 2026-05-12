





import java.util.List;
import java.util.ArrayList;

public class BibText_BibTextEntry extends LocatedElement {

    private String key;





    private BibText_BibTextFile bibtext_bibtextfile;


    public BibText_BibTextEntry(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public BibText_BibTextFile getBibtext_bibtextfile() {
        return bibtext_bibtextfile;
    }

    public void setBibtext_bibtextfile(BibText_BibTextFile bibtext_bibtextfile) {
        this.bibtext_bibtextfile = bibtext_bibtextfile;
    }

}