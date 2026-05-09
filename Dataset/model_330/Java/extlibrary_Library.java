





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Library extends Addressable {

    private String people;
    private String name;





    private List<extlibrary_Employee> extlibrary_employees;




    private List<extlibrary_Writer> extlibrary_writers;




    private List<extlibrary_Borrower> extlibrary_borrowers;




    private List<extlibrary_Book> extlibrary_books;


    public extlibrary_Library(
        String people,        String name    ) {
        super(
        );
        this.people = people;
        this.name = name;
        this.extlibrary_employees = new ArrayList<>();
        this.extlibrary_writers = new ArrayList<>();
        this.extlibrary_borrowers = new ArrayList<>();
        this.extlibrary_books = new ArrayList<>();
    }

    public extlibrary_Library(
        String people,        String name        ArrayList<extlibrary_Employee> extlibrary_employees,        ArrayList<extlibrary_Writer> extlibrary_writers,        ArrayList<extlibrary_Borrower> extlibrary_borrowers,        ArrayList<extlibrary_Book> extlibrary_books    ) {
        this.people = people;
        this.name = name;
        this.extlibrary_employees = extlibrary_employees;
        this.extlibrary_writers = extlibrary_writers;
        this.extlibrary_borrowers = extlibrary_borrowers;
        this.extlibrary_books = extlibrary_books;
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

    public List<extlibrary_Employee> getExtlibrary_employees() {
        return extlibrary_employees;
    }

    public void addExtlibrary_employee(Extlibrary_employee extlibrary_employee) {
        this.extlibrary_employees.add(extlibrary_employee);
    }
    public List<extlibrary_Writer> getExtlibrary_writers() {
        return extlibrary_writers;
    }

    public void addExtlibrary_writer(Extlibrary_writer extlibrary_writer) {
        this.extlibrary_writers.add(extlibrary_writer);
    }
    public List<extlibrary_Borrower> getExtlibrary_borrowers() {
        return extlibrary_borrowers;
    }

    public void addExtlibrary_borrower(Extlibrary_borrower extlibrary_borrower) {
        this.extlibrary_borrowers.add(extlibrary_borrower);
    }
    public List<extlibrary_Book> getExtlibrary_books() {
        return extlibrary_books;
    }

    public void addExtlibrary_book(Extlibrary_book extlibrary_book) {
        this.extlibrary_books.add(extlibrary_book);
    }

}