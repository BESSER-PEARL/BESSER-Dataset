





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Person  {

    private String SSNumber;
    private String gender;
    private String name;
    private String street;
    private String city;
    private String country;
    private String title;
    private String postalCode;
    private String phoneNumber;



    public HotelManagementClassDiagram_Person(
        String SSNumber,        String gender,        String name,        String street,        String city,        String country,        String title,        String postalCode,        String phoneNumber    ) {
        this.SSNumber = SSNumber;
        this.gender = gender;
        this.name = name;
        this.street = street;
        this.city = city;
        this.country = country;
        this.title = title;
        this.postalCode = postalCode;
        this.phoneNumber = phoneNumber;
    }


    public String getSsnumber() {
        return SSNumber;
    }

    public void setSsnumber(String SSNumber) {
        this.SSNumber = SSNumber;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}