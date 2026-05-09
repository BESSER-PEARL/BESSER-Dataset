





import java.util.List;
import java.util.ArrayList;

public class jointPackage_BibTeX2DocBook_SrcBook extends SrcDatedEntry, SrcTitledEntry, SrcAuthoredEntry {

    private String publisher;



    public jointPackage_BibTeX2DocBook_SrcBook(
        String publisher    ) {
        super(
        );
        this.publisher = publisher;
    }


    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }


}