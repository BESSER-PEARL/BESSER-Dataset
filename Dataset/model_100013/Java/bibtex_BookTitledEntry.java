





import java.util.List;
import java.util.ArrayList;

public class bibtex_BookTitledEntry extends BibTeXEntry {

    private String booktitle;



    public bibtex_BookTitledEntry(
        String booktitle    ) {
        super(
        );
        this.booktitle = booktitle;
    }


    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }


}