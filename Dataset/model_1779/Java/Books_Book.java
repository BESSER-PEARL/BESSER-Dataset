





import java.util.List;
import java.util.ArrayList;

public class Books_Book  {

    private String title;
    private String collecName;





    private Books_System books_system;


    public Books_Book(
        String title,        String collecName    ) {
        this.title = title;
        this.collecName = collecName;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCollecname() {
        return collecName;
    }

    public void setCollecname(String collecName) {
        this.collecName = collecName;
    }

    public Books_System getBooks_system() {
        return books_system;
    }

    public void setBooks_system(Books_System books_system) {
        this.books_system = books_system;
    }

}