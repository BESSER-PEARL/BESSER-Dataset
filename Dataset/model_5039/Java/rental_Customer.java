





import java.util.List;
import java.util.ArrayList;

public class rental_Customer  {

    private String firstName;
    private String lastName;





    private rental_RentalAgency rental_rentalagency;




    private rental_Address rental_address;




    private rental_RentalAgency rental_rentalagency;




    private List<rental_License> rental_licenses;




    private rental_License rental_license;


    public rental_Customer(
        String firstName,        String lastName    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.rental_licenses = new ArrayList<>();
    }

    public rental_Customer(
        String firstName,        String lastName        ArrayList<rental_License> rental_licenses    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.rental_licenses = rental_licenses;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
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
    public List<rental_License> getRental_licenses() {
        return rental_licenses;
    }

    public void addRental_license(Rental_license rental_license) {
        this.rental_licenses.add(rental_license);
    }
    public rental_License getRental_license() {
        return rental_license;
    }

    public void setRental_license(rental_License rental_license) {
        this.rental_license = rental_license;
    }

}