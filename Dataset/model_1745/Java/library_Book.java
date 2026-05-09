





import java.util.List;
import java.util.ArrayList;

public class library_Book extends Borrowable {

    private String author;



    public library_Book(
        String author    ) {
        super(
        );
        this.author = author;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}