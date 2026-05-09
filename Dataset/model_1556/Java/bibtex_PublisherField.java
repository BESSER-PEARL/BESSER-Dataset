





import java.util.List;
import java.util.ArrayList;

public class bibtex_PublisherField extends StringValue, Field {






    private bibtex_InProceedingsEntry bibtex_inproceedingsentry;


    public bibtex_PublisherField(
    ) {
        super(
        );
    }



    public bibtex_InProceedingsEntry getBibtex_inproceedingsentry() {
        return bibtex_inproceedingsentry;
    }

    public void setBibtex_inproceedingsentry(bibtex_InProceedingsEntry bibtex_inproceedingsentry) {
        this.bibtex_inproceedingsentry = bibtex_inproceedingsentry;
    }

}