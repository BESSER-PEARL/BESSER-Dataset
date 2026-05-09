





import java.util.List;
import java.util.ArrayList;

public class bibTeX_BookTitledEntry extends BibTeXEntry {

    private String booktitle;



    public bibTeX_BookTitledEntry(
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