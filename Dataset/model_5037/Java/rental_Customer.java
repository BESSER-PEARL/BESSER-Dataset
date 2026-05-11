





import java.util.List;
import java.util.ArrayList;

public class rental_Customer  {

    private String lastName;
    private String firstName;





    private rental_Address rental_address;




    private rental_RentalAgency rental_rentalagency;




    private rental_RentalAgency rental_rentalagency;


    public rental_Customer(
        String lastName,        String firstName    ) {
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public rental_Address getRental_address() {
        return rental_address;
    }

    public void setRental_address(rental_Address rental_address) {
        this.rental_address = rental_address;
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