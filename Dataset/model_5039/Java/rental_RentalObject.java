





import java.util.List;
import java.util.ArrayList;

public class rental_RentalObject  {

    private String name;
    private String picture;
    private String ID;





    private rental_RentalAgency rental_rentalagency;




    private rental_RentalAgency rental_rentalagency;


    public rental_RentalObject(
        String name,        String picture,        String ID    ) {
        this.name = name;
        this.picture = picture;
        this.ID = ID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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