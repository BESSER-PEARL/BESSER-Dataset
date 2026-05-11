





import java.util.List;
import java.util.ArrayList;

public class rental_RentalObject  {

    private String name;
    private String ID;
    private boolean available;





    private rental_RentalAgency rental_rentalagency;




    private rental_RentalAgency rental_rentalagency;


    public rental_RentalObject(
        String name,        String ID,        boolean available    ) {
        this.name = name;
        this.ID = ID;
        this.available = available;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public boolean getAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }

    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }
    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }

}