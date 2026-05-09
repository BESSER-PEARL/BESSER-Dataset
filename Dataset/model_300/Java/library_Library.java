





import java.util.List;
import java.util.ArrayList;

public class library_Library extends Addressable {

    private String name;
    private String people;





    private List<library_Employee> library_employees;




    private List<library_Writer> library_writers;




    private List<library_Borrower> library_borrowers;




    private library_Library library_library;




    private library_Library library_library;




    private List<library_Item> library_items;




    private List<library_Book> library_books;


    public library_Library(
        String name,        String people    ) {
        super(
        );
        this.name = name;
        this.people = people;
        this.library_employees = new ArrayList<>();
        this.library_writers = new ArrayList<>();
        this.library_borrowers = new ArrayList<>();
        this.library_items = new ArrayList<>();
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        String name,        String people        ArrayList<library_Employee> library_employees,        ArrayList<library_Writer> library_writers,        ArrayList<library_Borrower> library_borrowers,        ArrayList<library_Item> library_items,        ArrayList<library_Book> library_books    ) {
        this.name = name;
        this.people = people;
        this.library_employees = library_employees;
        this.library_writers = library_writers;
        this.library_borrowers = library_borrowers;
        this.library_items = library_items;
        this.library_books = library_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPeople() {
        return people;
    }

    public void setPeople(String people) {
        this.people = people;
    }

    public List<library_Employee> getLibrary_employees() {
        return library_employees;
    }

    public void addLibrary_employee(Library_employee library_employee) {
        this.library_employees.add(library_employee);
    }
    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }
    public List<library_Borrower> getLibrary_borrowers() {
        return library_borrowers;
    }

    public void addLibrary_borrower(Library_borrower library_borrower) {
        this.library_borrowers.add(library_borrower);
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
    public List<library_Item> getLibrary_items() {
        return library_items;
    }

    public void addLibrary_item(Library_item library_item) {
        this.library_items.add(library_item);
    }
    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}