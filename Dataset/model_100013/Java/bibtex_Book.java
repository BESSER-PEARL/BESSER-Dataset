





import java.util.List;
import java.util.ArrayList;

public class bibtex_Book extends TitledEntry, DatedEntry, AuthoredEntry {

    private String publisher;



    public bibtex_Book(
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