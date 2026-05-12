





import java.util.List;
import java.util.ArrayList;

public class bibtex_Note  {

    private String note;





    private bibtex_BibType bibtex_bibtype;


    public bibtex_Note(
        String note    ) {
        this.note = note;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public bibtex_BibType getBibtex_bibtype() {
        return bibtex_bibtype;
    }

    public void setBibtex_bibtype(bibtex_BibType bibtex_bibtype) {
        this.bibtex_bibtype = bibtex_bibtype;
    }

}