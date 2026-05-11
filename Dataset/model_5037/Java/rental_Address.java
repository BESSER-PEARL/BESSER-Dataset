





import java.util.List;
import java.util.ArrayList;

public class rental_Address  {

    private int number;
    private String streetType;
    private String city;
    private String zipCode;
    private String streetName;





    private rental_RentalAgency rental_rentalagency;


    public rental_Address(
        int number,        String streetType,        String city,        String zipCode,        String streetName    ) {
        this.number = number;
        this.streetType = streetType;
        this.city = city;
        this.zipCode = zipCode;
        this.streetName = streetName;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getStreettype() {
        return streetType;
    }

    public void setStreettype(String streetType) {
        this.streetType = streetType;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getStreetname() {
        return streetName;
    }

    public void setStreetname(String streetName) {
        this.streetName = streetName;
    }

    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }

}