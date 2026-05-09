





import java.util.List;
import java.util.ArrayList;

public class BibTeX_BookTitledEntry extends BibTeXEntry {

    private String booktitle;



    public BibTeX_BookTitledEntry(
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