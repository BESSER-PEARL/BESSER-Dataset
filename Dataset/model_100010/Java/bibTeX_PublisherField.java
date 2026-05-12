





import java.util.List;
import java.util.ArrayList;

public class bibTeX_PublisherField  {

    private String publisher;





    private bibTeX_Book bibtex_book;


    public bibTeX_PublisherField(
        String publisher    ) {
        this.publisher = publisher;
    }


    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }

    public bibTeX_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibTeX_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }

}