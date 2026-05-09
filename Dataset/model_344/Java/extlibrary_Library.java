





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Library extends Addressable {

    private String name;
    private String people;





    private List<extlibrary_Employee> extlibrary_employees;




    private List<extlibrary_Book> extlibrary_books;




    private List<extlibrary_Borrower> extlibrary_borrowers;




    private List<extlibrary_Item> extlibrary_items;




    private extlibrary_Library extlibrary_library;




    private List<extlibrary_Library> extlibrary_librarys;




    private List<extlibrary_Writer> extlibrary_writers;


    public extlibrary_Library(
        String name,        String people    ) {
        super(
        );
        this.name = name;
        this.people = people;
        this.extlibrary_employees = new ArrayList<>();
        this.extlibrary_books = new ArrayList<>();
        this.extlibrary_borrowers = new ArrayList<>();
        this.extlibrary_items = new ArrayList<>();
        this.extlibrary_librarys = new ArrayList<>();
        this.extlibrary_writers = new ArrayList<>();
    }

    public extlibrary_Library(
        String name,        String people        ArrayList<extlibrary_Employee> extlibrary_employees,        ArrayList<extlibrary_Book> extlibrary_books,        ArrayList<extlibrary_Borrower> extlibrary_borrowers,        ArrayList<extlibrary_Item> extlibrary_items,        ArrayList<extlibrary_Library> extlibrary_librarys,        ArrayList<extlibrary_Writer> extlibrary_writers    ) {
        this.name = name;
        this.people = people;
        this.extlibrary_employees = extlibrary_employees;
        this.extlibrary_books = extlibrary_books;
        this.extlibrary_borrowers = extlibrary_borrowers;
        this.extlibrary_items = extlibrary_items;
        this.extlibrary_librarys = extlibrary_librarys;
        this.extlibrary_writers = extlibrary_writers;
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

    public List<extlibrary_Employee> getExtlibrary_employees() {
        return extlibrary_employees;
    }

    public void addExtlibrary_employee(Extlibrary_employee extlibrary_employee) {
        this.extlibrary_employees.add(extlibrary_employee);
    }
    public List<extlibrary_Book> getExtlibrary_books() {
        return extlibrary_books;
    }

    public void addExtlibrary_book(Extlibrary_book extlibrary_book) {
        this.extlibrary_books.add(extlibrary_book);
    }
    public List<extlibrary_Borrower> getExtlibrary_borrowers() {
        return extlibrary_borrowers;
    }

    public void addExtlibrary_borrower(Extlibrary_borrower extlibrary_borrower) {
        this.extlibrary_borrowers.add(extlibrary_borrower);
    }
    public List<extlibrary_Item> getExtlibrary_items() {
        return extlibrary_items;
    }

    public void addExtlibrary_item(Extlibrary_item extlibrary_item) {
        this.extlibrary_items.add(extlibrary_item);
    }
    public extlibrary_Library getExtlibrary_library() {
        return extlibrary_library;
    }

    public void setExtlibrary_library(extlibrary_Library extlibrary_library) {
        this.extlibrary_library = extlibrary_library;
    }
    public List<extlibrary_Library> getExtlibrary_librarys() {
        return extlibrary_librarys;
    }

    public void addExtlibrary_library(Extlibrary_library extlibrary_library) {
        this.extlibrary_librarys.add(extlibrary_library);
    }
    public List<extlibrary_Writer> getExtlibrary_writers() {
        return extlibrary_writers;
    }

    public void addExtlibrary_writer(Extlibrary_writer extlibrary_writer) {
        this.extlibrary_writers.add(extlibrary_writer);
    }

}