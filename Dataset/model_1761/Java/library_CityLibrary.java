





import java.util.List;
import java.util.ArrayList;

public class library_CityLibrary  {

    private String address;





    private library_Borrowable library_borrowable;




    private List<library_Borrowable> library_borrowables;




    private List<library_Customer> library_customers;


    public library_CityLibrary(
        String address    ) {
        this.address = address;
        this.library_borrowables = new ArrayList<>();
        this.library_customers = new ArrayList<>();
    }

    public library_CityLibrary(
        String address        ArrayList<library_Borrowable> library_borrowables,        ArrayList<library_Customer> library_customers    ) {
        this.address = address;
        this.library_borrowables = library_borrowables;
        this.library_customers = library_customers;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public library_Borrowable getLibrary_borrowable() {
        return library_borrowable;
    }

    public void setLibrary_borrowable(library_Borrowable library_borrowable) {
        this.library_borrowable = library_borrowable;
    }
    public List<library_Borrowable> getLibrary_borrowables() {
        return library_borrowables;
    }

    public void addLibrary_borrowable(Library_borrowable library_borrowable) {
        this.library_borrowables.add(library_borrowable);
    }
    public List<library_Customer> getLibrary_customers() {
        return library_customers;
    }

    public void addLibrary_customer(Library_customer library_customer) {
        this.library_customers.add(library_customer);
    }

}