





import java.util.List;
import java.util.ArrayList;

public class bibTeX_EditionField  {

    private String edition;





    private bibTeX_Book bibtex_book;


    public bibTeX_EditionField(
        String edition    ) {
        this.edition = edition;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }

    public bibTeX_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibTeX_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }

}