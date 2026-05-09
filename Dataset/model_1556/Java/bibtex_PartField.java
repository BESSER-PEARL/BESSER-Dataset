





import java.util.List;
import java.util.ArrayList;

public class bibtex_PartField extends IntValue, Field {






    private bibtex_ArticleEntry bibtex_articleentry;


    public bibtex_PartField(
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

}