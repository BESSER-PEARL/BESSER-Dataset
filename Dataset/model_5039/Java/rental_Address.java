





import java.util.List;
import java.util.ArrayList;

public class rental_Address  {

    private int number;
    private String zipCode;
    private String streetName;
    private String city;
    private String streetType;



    public rental_Address(
        int number,        String zipCode,        String streetName,        String city,        String streetType    ) {
        this.number = number;
        this.zipCode = zipCode;
        this.streetName = streetName;
        this.city = city;
        this.streetType = streetType;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
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


}