





import java.util.List;
import java.util.ArrayList;

public class rental_RentalObject  {

    private String picture;
    private String name;
    private String ID;





    private rental_RentalAgency rental_rentalagency;




    private rental_RentalAgency rental_rentalagency;


    public rental_RentalObject(
        String picture,        String name,        String ID    ) {
        this.picture = picture;
        this.name = name;
        this.ID = ID;
    }


    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
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