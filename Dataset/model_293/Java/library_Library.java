





import java.util.List;
import java.util.ArrayList;

public class library_Library extends Identifiable {

    private String name;





    private List<library_Book> library_books;


    public library_Library(
        String name    ) {
        super(
        );
        this.name = name;
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Book> library_books    ) {
        this.name = name;
        this.library_books = library_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}