





import java.util.List;
import java.util.ArrayList;

public class library_Library  {






    private List<library_Author> library_authors;




    private List<library_Book> library_books;


    public library_Library(
    ) {
        this.library_authors = new ArrayList<>();
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        ArrayList<library_Author> library_authors,        ArrayList<library_Book> library_books    ) {
        this.library_authors = library_authors;
        this.library_books = library_books;
    }


    public List<library_Author> getLibrary_authors() {
        return library_authors;
    }

    public void addLibrary_author(Library_author library_author) {
        this.library_authors.add(library_author);
    }
    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}