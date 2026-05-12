





import java.util.List;
import java.util.ArrayList;

public class bibTeX_Article extends BibtexEntryTypes {






    private bibTeX_AuthorField bibtex_authorfield;


    public bibTeX_Article(
    ) {
        super(
        );
    }



    public bibTeX_AuthorField getBibtex_authorfield() {
        return bibtex_authorfield;
    }

    public void setBibtex_authorfield(bibTeX_AuthorField bibtex_authorfield) {
        this.bibtex_authorfield = bibtex_authorfield;
    }

}