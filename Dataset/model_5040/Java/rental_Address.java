





import java.util.List;
import java.util.ArrayList;

public class rental_Address  {

    private String zipCode;
    private String city;
    private String streetName;
    private int number;
    private String streetType;





    private rental_RentalAgency rental_rentalagency;




    private rental_Customer rental_customer;


    public rental_Address(
        String zipCode,        String city,        String streetName,        int number,        String streetType    ) {
        this.zipCode = zipCode;
        this.city = city;
        this.streetName = streetName;
        this.number = number;
        this.streetType = streetType;
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
    public String getStreetname() {
        return streetName;
    }

    public void setStreetname(String streetName) {
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

    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }
    public rental_Customer getRental_customer() {
        return rental_customer;
    }

    public void setRental_customer(rental_Customer rental_customer) {
        this.rental_customer = rental_customer;
    }

}