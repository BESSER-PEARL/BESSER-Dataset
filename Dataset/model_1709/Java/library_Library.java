





import java.util.List;
import java.util.ArrayList;

public class library_Library  {






    private library_Book library_book;




    private List<library_Author> library_authors;


    public library_Library(
    ) {
        this.library_authors = new ArrayList<>();
    }

    public library_Library(
        ArrayList<library_Author> library_authors    ) {
        this.library_authors = library_authors;
    }


    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }
    public List<library_Author> getLibrary_authors() {
        return library_authors;
    }

    public void addLibrary_author(Library_author library_author) {
        this.library_authors.add(library_author);
    }

}