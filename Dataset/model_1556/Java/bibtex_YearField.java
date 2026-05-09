





import java.util.List;
import java.util.ArrayList;

public class bibtex_YearField extends YearValue, Field {






    private bibtex_ArticleEntry bibtex_articleentry;




    private bibtex_InProceedingsEntry bibtex_inproceedingsentry;


    public bibtex_YearField(
    ) {
        super(
        );
    }



    public bibtex_ArticleEntry getBibtex_articleentry() {
        return bibtex_articleentry;
    }

    public void setBibtex_articleentry(bibtex_ArticleEntry bibtex_articleentry) {
        this.bibtex_articleentry = bibtex_articleentry;
    }
    public bibtex_InProceedingsEntry getBibtex_inproceedingsentry() {
        return bibtex_inproceedingsentry;
    }

    public void setBibtex_inproceedingsentry(bibtex_InProceedingsEntry bibtex_inproceedingsentry) {
        this.bibtex_inproceedingsentry = bibtex_inproceedingsentry;
    }

}