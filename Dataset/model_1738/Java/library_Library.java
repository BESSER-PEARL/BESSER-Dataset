





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;





    private List<library_Book> library_books;




    private List<library_Person> library_persons;


    public library_Library(
        String name    ) {
        this.name = name;
        this.library_books = new ArrayList<>();
        this.library_persons = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Book> library_books,        ArrayList<library_Person> library_persons    ) {
        this.name = name;
        this.library_books = library_books;
        this.library_persons = library_persons;
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
    public List<library_Person> getLibrary_persons() {
        return library_persons;
    }

    public void addLibrary_person(Library_person library_person) {
        this.library_persons.add(library_person);
    }

}