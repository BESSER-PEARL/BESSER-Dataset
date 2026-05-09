





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Library  {






    private List<library3Simplified_Customer> library3simplified_customers;


    public library3Simplified_Library(
    ) {
        this.library3simplified_customers = new ArrayList<>();
    }

    public library3Simplified_Library(
        ArrayList<library3Simplified_Customer> library3simplified_customers    ) {
        this.library3simplified_customers = library3simplified_customers;
    }


    public List<library3Simplified_Customer> getLibrary3simplified_customers() {
        return library3simplified_customers;
    }

    public void addLibrary3simplified_customer(Library3simplified_customer library3simplified_customer) {
        this.library3simplified_customers.add(library3simplified_customer);
    }

}