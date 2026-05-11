





import java.util.List;
import java.util.ArrayList;

public class fair_Person  {

    private String name;
    private String street;
    private String email;
    private String city;
    private String lastName;
    private String phone;
    private int exhibitorNumber;
    private String pin;
    private String state;
    private String firstName;
    private String comments;
    private int salesOrder;
    private String zipCode;



    public fair_Person(
        String name,        String street,        String email,        String city,        String lastName,        String phone,        int exhibitorNumber,        String pin,        String state,        String firstName,        String comments,        int salesOrder,        String zipCode    ) {
        this.name = name;
        this.street = street;
        this.email = email;
        this.city = city;
        this.lastName = lastName;
        this.phone = phone;
        this.exhibitorNumber = exhibitorNumber;
        this.pin = pin;
        this.state = state;
        this.firstName = firstName;
        this.comments = comments;
        this.salesOrder = salesOrder;
        this.zipCode = zipCode;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public int getExhibitornumber() {
        return exhibitorNumber;
    }

    public void setExhibitornumber(int exhibitorNumber) {
        this.exhibitorNumber = exhibitorNumber;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public int getSalesorder() {
        return salesOrder;
    }

    public void setSalesorder(int salesOrder) {
        this.salesOrder = salesOrder;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }


}