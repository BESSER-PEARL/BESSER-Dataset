





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_BookTitledEntry extends Entry {

    private String booktitle;



    public BIBTEXML_BookTitledEntry(
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