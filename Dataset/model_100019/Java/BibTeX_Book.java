





import java.util.List;
import java.util.ArrayList;

public class BibTeX_Book extends AuthoredEntry, TitledEntry, DatedEntry {

    private String publisher;



    public BibTeX_Book(
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