





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Library extends Addressable {

    private String name;





    private List<extlibrary_Writer> extlibrary_writers;




    private List<extlibrary_Person> extlibrary_persons;




    private List<extlibrary_Book> extlibrary_books;




    private List<extlibrary_Employee> extlibrary_employees;




    private List<extlibrary_Borrower> extlibrary_borrowers;




    private extlibrary_Library extlibrary_library;




    private List<extlibrary_Library> extlibrary_librarys;




    private List<extlibrary_Person> extlibrary_persons;


    public extlibrary_Library(
        String name    ) {
        super(
        );
        this.name = name;
        this.extlibrary_writers = new ArrayList<>();
        this.extlibrary_persons = new ArrayList<>();
        this.extlibrary_books = new ArrayList<>();
        this.extlibrary_employees = new ArrayList<>();
        this.extlibrary_borrowers = new ArrayList<>();
        this.extlibrary_librarys = new ArrayList<>();
        this.extlibrary_persons = new ArrayList<>();
    }

    public extlibrary_Library(
        String name        ArrayList<extlibrary_Writer> extlibrary_writers,        ArrayList<extlibrary_Person> extlibrary_persons,        ArrayList<extlibrary_Book> extlibrary_books,        ArrayList<extlibrary_Employee> extlibrary_employees,        ArrayList<extlibrary_Borrower> extlibrary_borrowers,        ArrayList<extlibrary_Library> extlibrary_librarys,        ArrayList<extlibrary_Person> extlibrary_persons    ) {
        this.name = name;
        this.extlibrary_writers = extlibrary_writers;
        this.extlibrary_persons = extlibrary_persons;
        this.extlibrary_books = extlibrary_books;
        this.extlibrary_employees = extlibrary_employees;
        this.extlibrary_borrowers = extlibrary_borrowers;
        this.extlibrary_librarys = extlibrary_librarys;
        this.extlibrary_persons = extlibrary_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<extlibrary_Writer> getExtlibrary_writers() {
        return extlibrary_writers;
    }

    public void addExtlibrary_writer(Extlibrary_writer extlibrary_writer) {
        this.extlibrary_writers.add(extlibrary_writer);
    }
    public List<extlibrary_Person> getExtlibrary_persons() {
        return extlibrary_persons;
    }

    public void addExtlibrary_person(Extlibrary_person extlibrary_person) {
        this.extlibrary_persons.add(extlibrary_person);
    }
    public List<extlibrary_Book> getExtlibrary_books() {
        return extlibrary_books;
    }

    public void addExtlibrary_book(Extlibrary_book extlibrary_book) {
        this.extlibrary_books.add(extlibrary_book);
    }
    public List<extlibrary_Employee> getExtlibrary_employees() {
        return extlibrary_employees;
    }

    public void addExtlibrary_employee(Extlibrary_employee extlibrary_employee) {
        this.extlibrary_employees.add(extlibrary_employee);
    }
    public List<extlibrary_Borrower> getExtlibrary_borrowers() {
        return extlibrary_borrowers;
    }

    public void addExtlibrary_borrower(Extlibrary_borrower extlibrary_borrower) {
        this.extlibrary_borrowers.add(extlibrary_borrower);
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
    public List<extlibrary_Person> getExtlibrary_persons() {
        return extlibrary_persons;
    }

    public void addExtlibrary_person(Extlibrary_person extlibrary_person) {
        this.extlibrary_persons.add(extlibrary_person);
    }

}