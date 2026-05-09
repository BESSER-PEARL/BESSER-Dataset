





import java.util.List;
import java.util.ArrayList;

public class library_Writer  {

    private String name;





    private library_Book library_book;




    private library_Library library_library;




    private List<library_Book> library_books;


    public library_Writer(
        String name    ) {
        this.name = name;
        this.library_books = new ArrayList<>();
    }

    public library_Writer(
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

    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}