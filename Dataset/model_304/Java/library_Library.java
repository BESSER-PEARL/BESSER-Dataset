





import java.util.List;
import java.util.ArrayList;

public class library_Library  {






    private List<library_Writer> library_writers;




    private List<library_Book> library_books;


    public library_Library(
    ) {
        this.library_writers = new ArrayList<>();
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        ArrayList<library_Writer> library_writers,        ArrayList<library_Book> library_books    ) {
        this.library_writers = library_writers;
        this.library_books = library_books;
    }


    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }
    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}