





import java.util.List;
import java.util.ArrayList;

public class library_Library  {






    private List<library_Book> library_books;


    public library_Library(
    ) {
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        ArrayList<library_Book> library_books    ) {
        this.library_books = library_books;
    }


    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}