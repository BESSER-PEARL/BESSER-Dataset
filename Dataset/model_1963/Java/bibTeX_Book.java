





import java.util.List;
import java.util.ArrayList;

public class bibTeX_Book extends BibtexEntryTypes {






    private bibTeX_IsbnField bibtex_isbnfield;


    public bibTeX_Book(
    ) {
        super(
        );
    }



    public bibTeX_IsbnField getBibtex_isbnfield() {
        return bibtex_isbnfield;
    }

    public void setBibtex_isbnfield(bibTeX_IsbnField bibtex_isbnfield) {
        this.bibtex_isbnfield = bibtex_isbnfield;
    }

}