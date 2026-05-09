





import java.util.List;
import java.util.ArrayList;

public class library_Library extends Addressable {

    private String people;
    private String name;





    private List<library_Writer> library_writers;




    private List<library_Book> library_books;




    private library_Library library_library;




    private library_Library library_library;


    public library_Library(
        String people,        String name    ) {
        super(
        );
        this.people = people;
        this.name = name;
        this.library_writers = new ArrayList<>();
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        String people,        String name        ArrayList<library_Writer> library_writers,        ArrayList<library_Book> library_books    ) {
        this.people = people;
        this.name = name;
        this.library_writers = library_writers;
        this.library_books = library_books;
    }

    public String getPeople() {
        return people;
    }

    public void setPeople(String people) {
        this.people = people;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}