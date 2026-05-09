





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;





    private List<library_Book> library_books;




    private List<library_Writer> library_writers;


    public library_Library(
        String name    ) {
        this.name = name;
        this.library_books = new ArrayList<>();
        this.library_writers = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Book> library_books,        ArrayList<library_Writer> library_writers    ) {
        this.name = name;
        this.library_books = library_books;
        this.library_writers = library_writers;
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
    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }

}