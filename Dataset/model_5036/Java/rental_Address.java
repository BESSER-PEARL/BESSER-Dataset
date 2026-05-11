





import java.util.List;
import java.util.ArrayList;

public class rental_Address  {

    private int number;
    private String streetName;
    private String zipCode;
    private String city;
    private String streetType;





    private rental_RentalAgency rental_rentalagency;


    public rental_Address(
        int number,        String streetName,        String zipCode,        String city,        String streetType    ) {
        this.number = number;
        this.streetName = streetName;
        this.zipCode = zipCode;
        this.city = city;
        this.streetType = streetType;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getStreetname() {
        return streetName;
    }

    public void setStreetname(String streetName) {
        this.streetName = streetName;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getStreettype() {
        return streetType;
    }

    public void setStreettype(String streetType) {
        this.streetType = streetType;
    }

    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }

}