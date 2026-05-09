





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String address;





    private List<library_Customer> library_customers;




    private library_Borrowable library_borrowable;




    private library_Author library_author;




    private List<library_Author> library_authors;




    private List<library_Borrowable> library_borrowables;


    public library_Library(
        String address    ) {
        this.address = address;
        this.library_customers = new ArrayList<>();
        this.library_authors = new ArrayList<>();
        this.library_borrowables = new ArrayList<>();
    }

    public library_Library(
        String address        ArrayList<library_Customer> library_customers,        ArrayList<library_Author> library_authors,        ArrayList<library_Borrowable> library_borrowables    ) {
        this.address = address;
        this.library_customers = library_customers;
        this.library_authors = library_authors;
        this.library_borrowables = library_borrowables;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<library_Customer> getLibrary_customers() {
        return library_customers;
    }

    public void addLibrary_customer(Library_customer library_customer) {
        this.library_customers.add(library_customer);
    }
    public library_Borrowable getLibrary_borrowable() {
        return library_borrowable;
    }

    public void setLibrary_borrowable(library_Borrowable library_borrowable) {
        this.library_borrowable = library_borrowable;
    }
    public library_Author getLibrary_author() {
        return library_author;
    }

    public void setLibrary_author(library_Author library_author) {
        this.library_author = library_author;
    }
    public List<library_Author> getLibrary_authors() {
        return library_authors;
    }

    public void addLibrary_author(Library_author library_author) {
        this.library_authors.add(library_author);
    }
    public List<library_Borrowable> getLibrary_borrowables() {
        return library_borrowables;
    }

    public void addLibrary_borrowable(Library_borrowable library_borrowable) {
        this.library_borrowables.add(library_borrowable);
    }

}