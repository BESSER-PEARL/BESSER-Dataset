





import java.util.List;
import java.util.ArrayList;

public class fair_Person  {

    private int salesOrder;
    private String comments;
    private String phone;
    private String zipCode;
    private String street;
    private String lastName;
    private String name;
    private String city;
    private String state;
    private String firstName;
    private String pin;





    private fair_Fair fair_fair;




    private fair_YouthClub fair_youthclub;


    public fair_Person(
        int salesOrder,        String comments,        String phone,        String zipCode,        String street,        String lastName,        String name,        String city,        String state,        String firstName,        String pin    ) {
        this.salesOrder = salesOrder;
        this.comments = comments;
        this.phone = phone;
        this.zipCode = zipCode;
        this.street = street;
        this.lastName = lastName;
        this.name = name;
        this.city = city;
        this.state = state;
        this.firstName = firstName;
        this.pin = pin;
    }


    public int getSalesorder() {
        return salesOrder;
    }

    public void setSalesorder(int salesOrder) {
        this.salesOrder = salesOrder;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
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
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
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
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }

    public fair_Fair getFair_fair() {
        return fair_fair;
    }

    public void setFair_fair(fair_Fair fair_fair) {
        this.fair_fair = fair_fair;
    }
    public fair_YouthClub getFair_youthclub() {
        return fair_youthclub;
    }

    public void setFair_youthclub(fair_YouthClub fair_youthclub) {
        this.fair_youthclub = fair_youthclub;
    }

}