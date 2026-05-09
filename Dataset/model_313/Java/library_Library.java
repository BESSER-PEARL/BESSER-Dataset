





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;





    private List<library_Book> library_books;




    private List<Writer> writers;


    public library_Library(
        String name    ) {
        this.name = name;
        this.library_books = new ArrayList<>();
        this.writers = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Book> library_books,        ArrayList<Writer> writers    ) {
        this.name = name;
        this.library_books = library_books;
        this.writers = writers;
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
    public List<Writer> getWriters() {
        return writers;
    }

    public void addWriter(Writer writer) {
        this.writers.add(writer);
    }

}