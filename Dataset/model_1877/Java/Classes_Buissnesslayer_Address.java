





import java.util.List;
import java.util.ArrayList;

public class Classes_Buissnesslayer_Address  {

    private String street;
    private int postalNumber;
    private String country;
    private String city;



    public Classes_Buissnesslayer_Address(
        String street,        int postalNumber,        String country,        String city    ) {
        this.street = street;
        this.postalNumber = postalNumber;
        this.country = country;
        this.city = city;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public int getPostalnumber() {
        return postalNumber;
    }

    public void setPostalnumber(int postalNumber) {
        this.postalNumber = postalNumber;
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


}