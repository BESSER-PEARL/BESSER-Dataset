





import java.util.List;
import java.util.ArrayList;

public class newClasses_Customer extends Booker {

    private String city;
    private String zipCode;
    private String phoneNum;
    private String email;
    private String personalNum;
    private String bookingCost;
    private String firstName;
    private String address;
    private String bookingNum;
    private String lastName;
    private String country;



    public newClasses_Customer(
        String city,        String zipCode,        String phoneNum,        String email,        String personalNum,        String bookingCost,        String firstName,        String address,        String bookingNum,        String lastName,        String country    ) {
        super(
        );
        this.city = city;
        this.zipCode = zipCode;
        this.phoneNum = phoneNum;
        this.email = email;
        this.personalNum = personalNum;
        this.bookingCost = bookingCost;
        this.firstName = firstName;
        this.address = address;
        this.bookingNum = bookingNum;
        this.lastName = lastName;
        this.country = country;
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
    public String getPhonenum() {
        return phoneNum;
    }

    public void setPhonenum(String phoneNum) {
        this.phoneNum = phoneNum;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPersonalnum() {
        return personalNum;
    }

    public void setPersonalnum(String personalNum) {
        this.personalNum = personalNum;
    }
    public String getBookingcost() {
        return bookingCost;
    }

    public void setBookingcost(String bookingCost) {
        this.bookingCost = bookingCost;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getBookingnum() {
        return bookingNum;
    }

    public void setBookingnum(String bookingNum) {
        this.bookingNum = bookingNum;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }


}