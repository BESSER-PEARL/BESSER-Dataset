





import java.util.List;
import java.util.ArrayList;

public class resourceunload_Library  {

    private String name;





    private List<resourceunload_Book> resourceunload_books;


    public resourceunload_Library(
        String name    ) {
        this.name = name;
        this.resourceunload_books = new ArrayList<>();
    }

    public resourceunload_Library(
        String name        ArrayList<resourceunload_Book> resourceunload_books    ) {
        this.name = name;
        this.resourceunload_books = resourceunload_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<resourceunload_Book> getResourceunload_books() {
        return resourceunload_books;
    }

    public void addResourceunload_book(Resourceunload_book resourceunload_book) {
        this.resourceunload_books.add(resourceunload_book);
    }

}