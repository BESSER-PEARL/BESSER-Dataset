





import java.util.List;
import java.util.ArrayList;

public class bibTeX_Book extends DatedEntry, TitledEntry, AuthoredEntry {

    private String publisher;



    public bibTeX_Book(
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