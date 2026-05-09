





import java.util.List;
import java.util.ArrayList;

public class library_Book extends Borrowable {






    private List<library_Author> library_authors;




    private library_Author library_author;


    public library_Book(
    ) {
        super(
        );
        this.library_authors = new ArrayList<>();
    }

    public library_Book(
        ArrayList<library_Author> library_authors    ) {
        this.library_authors = library_authors;
    }


    public List<library_Author> getLibrary_authors() {
        return library_authors;
    }

    public void addLibrary_author(Library_author library_author) {
        this.library_authors.add(library_author);
    }
    public library_Author getLibrary_author() {
        return library_author;
    }

    public void setLibrary_author(library_Author library_author) {
        this.library_author = library_author;
    }

}