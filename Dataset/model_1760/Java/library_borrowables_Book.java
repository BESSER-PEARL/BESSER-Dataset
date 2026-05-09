





import java.util.List;
import java.util.ArrayList;

public class library_borrowables_Book extends Borrowable {

    private String authors;



    public library_borrowables_Book(
        String authors    ) {
        super(
        );
        this.authors = authors;
    }


    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }


}