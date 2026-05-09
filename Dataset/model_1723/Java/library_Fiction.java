





import java.util.List;
import java.util.ArrayList;

public class library_Fiction  {

    private String Name;





    private List<library_Book> library_books;




    private library_Library library_library;


    public library_Fiction(
        String Name    ) {
        this.Name = Name;
        this.library_books = new ArrayList<>();
    }

    public library_Fiction(
        String Name        ArrayList<library_Book> library_books    ) {
        this.Name = Name;
        this.library_books = library_books;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}