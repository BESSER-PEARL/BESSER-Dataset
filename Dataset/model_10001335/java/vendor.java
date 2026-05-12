





import java.util.List;
import java.util.ArrayList;

public class vendor  {

    private String attribute;
    private String book_details;



    public vendor(
        String attribute,        String book_details    ) {
        this.attribute = attribute;
        this.book_details = book_details;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getBook_details() {
        return book_details;
    }

    public void setBook_details(String book_details) {
        this.book_details = book_details;
    }


}