





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Person  {

    private String country;
    private String postalCode;
    private String city;
    private String street;
    private String name;
    private String phoneNumber;
    private String SSNumber;
    private String title;
    private String gender;



    public HotelManagementClassDiagram_Person(
        String country,        String postalCode,        String city,        String street,        String name,        String phoneNumber,        String SSNumber,        String title,        String gender    ) {
        this.country = country;
        this.postalCode = postalCode;
        this.city = city;
        this.street = street;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.SSNumber = SSNumber;
        this.title = title;
        this.gender = gender;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getSsnumber() {
        return SSNumber;
    }

    public void setSsnumber(String SSNumber) {
        this.SSNumber = SSNumber;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }


}