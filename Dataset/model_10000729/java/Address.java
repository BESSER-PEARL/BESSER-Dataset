





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private int id;
    private String street;
    private String city;
    private String zipCode;
    private String country;





    private Position position;


    public Address(
        int id,        String street,        String city,        String zipCode,        String country    ) {
        this.id = id;
        this.street = street;
        this.city = city;
        this.zipCode = zipCode;
        this.country = country;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
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
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }

}