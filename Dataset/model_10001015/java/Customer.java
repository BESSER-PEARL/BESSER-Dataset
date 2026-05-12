





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String user_name;
    private String firstName;
    private int phoneNo;
    private String lastName;
    private String address;



    public Customer(
        String user_name,        String firstName,        int phoneNo,        String lastName,        String address    ) {
        this.user_name = user_name;
        this.firstName = firstName;
        this.phoneNo = phoneNo;
        this.lastName = lastName;
        this.address = address;
    }


    public String getUser_name() {
        return user_name;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public int getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(int phoneNo) {
        this.phoneNo = phoneNo;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}