





import java.util.List;
import java.util.ArrayList;

public class bibtex_BookTitleField extends StringValue, Field {






    private bibtex_InProceedingsEntry bibtex_inproceedingsentry;


    public bibtex_BookTitleField(
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