





import java.util.List;
import java.util.ArrayList;

public class fair_Person  {

    private String firstName;
    private String comments;
    private int salesOrder;
    private String lastName;
    private int exhibitorNumber;
    private String name;
    private String phone;
    private String street;
    private String state;
    private String city;
    private String pin;
    private String zipCode;
    private String email;





    private fair_Exhibit fair_exhibit;




    private fair_Fair fair_fair;




    private fair_YouthClub fair_youthclub;


    public fair_Person(
        String firstName,        String comments,        int salesOrder,        String lastName,        int exhibitorNumber,        String name,        String phone,        String street,        String state,        String city,        String pin,        String zipCode,        String email    ) {
        this.firstName = firstName;
        this.comments = comments;
        this.salesOrder = salesOrder;
        this.lastName = lastName;
        this.exhibitorNumber = exhibitorNumber;
        this.name = name;
        this.phone = phone;
        this.street = street;
        this.state = state;
        this.city = city;
        this.pin = pin;
        this.zipCode = zipCode;
        this.email = email;
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
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public int getExhibitornumber() {
        return exhibitorNumber;
    }

    public void setExhibitornumber(int exhibitorNumber) {
        this.exhibitorNumber = exhibitorNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public fair_Exhibit getFair_exhibit() {
        return fair_exhibit;
    }

    public void setFair_exhibit(fair_Exhibit fair_exhibit) {
        this.fair_exhibit = fair_exhibit;
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