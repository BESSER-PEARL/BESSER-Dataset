





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String city;
    private String zipCode;
    private String country;
    private String street;
    private int id;





    private Position position;


    public Address(
        String city,        String zipCode,        String country,        String street,        int id    ) {
        this.city = city;
        this.zipCode = zipCode;
        this.country = country;
        this.street = street;
        this.id = id;
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
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }

}