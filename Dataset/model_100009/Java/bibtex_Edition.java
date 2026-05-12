





import java.util.List;
import java.util.ArrayList;

public class bibtex_Edition  {

    private String edition;





    private bibtex_Book bibtex_book;




    private bibtex_Manual bibtex_manual;




    private bibtex_Inbook bibtex_inbook;


    public bibtex_Edition(
        String edition    ) {
        this.edition = edition;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }

    public bibtex_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibtex_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }
    public bibtex_Manual getBibtex_manual() {
        return bibtex_manual;
    }

    public void setBibtex_manual(bibtex_Manual bibtex_manual) {
        this.bibtex_manual = bibtex_manual;
    }
    public bibtex_Inbook getBibtex_inbook() {
        return bibtex_inbook;
    }

    public void setBibtex_inbook(bibtex_Inbook bibtex_inbook) {
        this.bibtex_inbook = bibtex_inbook;
    }

}