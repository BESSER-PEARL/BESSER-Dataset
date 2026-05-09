





import java.util.List;
import java.util.ArrayList;

public class libraryExample_Writer  {

    private String lastname;
    private String name;





    private List<libraryExample_Book> libraryexample_books;




    private libraryExample_Book libraryexample_book;




    private libraryExample_Library libraryexample_library;


    public libraryExample_Writer(
        String lastname,        String name    ) {
        this.lastname = lastname;
        this.name = name;
        this.libraryexample_books = new ArrayList<>();
    }

    public libraryExample_Writer(
        String lastname,        String name        ArrayList<libraryExample_Book> libraryexample_books    ) {
        this.lastname = lastname;
        this.name = name;
        this.libraryexample_books = libraryexample_books;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<libraryExample_Book> getLibraryexample_books() {
        return libraryexample_books;
    }

    public void addLibraryexample_book(Libraryexample_book libraryexample_book) {
        this.libraryexample_books.add(libraryexample_book);
    }
    public libraryExample_Book getLibraryexample_book() {
        return libraryexample_book;
    }

    public void setLibraryexample_book(libraryExample_Book libraryexample_book) {
        this.libraryexample_book = libraryexample_book;
    }
    public libraryExample_Library getLibraryexample_library() {
        return libraryexample_library;
    }

    public void setLibraryexample_library(libraryExample_Library libraryexample_library) {
        this.libraryexample_library = libraryexample_library;
    }

}