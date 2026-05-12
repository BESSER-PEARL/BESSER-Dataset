





import java.util.List;
import java.util.ArrayList;

public class BibText_Attribute extends LocatedElement {

    private String value;





    private BibText_BibTextEntry bibtext_bibtextentry;


    public BibText_Attribute(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public BibText_BibTextEntry getBibtext_bibtextentry() {
        return bibtext_bibtextentry;
    }

    public void setBibtext_bibtextentry(BibText_BibTextEntry bibtext_bibtextentry) {
        this.bibtext_bibtextentry = bibtext_bibtextentry;
    }

}