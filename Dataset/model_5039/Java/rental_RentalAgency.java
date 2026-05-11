





import java.util.List;
import java.util.ArrayList;

public class rental_RentalAgency  {

    private String name;





    private rental_Address rental_address;


    public rental_RentalAgency(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rental_Address getRental_address() {
        return rental_address;
    }

    public void setRental_address(rental_Address rental_address) {
        this.rental_address = rental_address;
    }

}