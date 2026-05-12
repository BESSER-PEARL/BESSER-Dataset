





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String country;
    private String city;
    private int id;
    private String zipCode;
    private String street;





    private Position position;


    public Address(
        String country,        String city,        int id,        String zipCode,        String street    ) {
        this.country = country;
        this.city = city;
        this.id = id;
        this.zipCode = zipCode;
        this.street = street;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }

}