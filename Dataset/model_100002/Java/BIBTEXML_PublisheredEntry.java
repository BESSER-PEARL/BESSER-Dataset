





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_PublisheredEntry extends Entry {

    private String publisher;



    public BIBTEXML_PublisheredEntry(
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