





import java.util.List;
import java.util.ArrayList;

public class jointPackage_SrcBookTitledEntry extends SrcBibTeXEntry {

    private String booktitle;



    public jointPackage_SrcBookTitledEntry(
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