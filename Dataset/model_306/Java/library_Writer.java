





import java.util.List;
import java.util.ArrayList;

public class library_Writer extends Person {






    private library_Book library_book;




    private List<library_Book> library_books;


    public library_Writer(
    ) {
        super(
        );
        this.library_books = new ArrayList<>();
    }

    public library_Writer(
        ArrayList<library_Book> library_books    ) {
        this.library_books = library_books;
    }


    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }
    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}