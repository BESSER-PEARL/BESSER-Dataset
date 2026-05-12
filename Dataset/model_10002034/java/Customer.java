





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String password;
    private String address;
    private String CCinfo;
    private String email;
    private String customerID;
    private String name;
    private int phoneNo;



    public Customer(
        String password,        String address,        String CCinfo,        String email,        String customerID,        String name,        int phoneNo    ) {
        this.password = password;
        this.address = address;
        this.CCinfo = CCinfo;
        this.email = email;
        this.customerID = customerID;
        this.name = name;
        this.phoneNo = phoneNo;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getCcinfo() {
        return CCinfo;
    }

    public void setCcinfo(String CCinfo) {
        this.CCinfo = CCinfo;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCustomerid() {
        return customerID;
    }

    public void setCustomerid(String customerID) {
        this.customerID = customerID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(int phoneNo) {
        this.phoneNo = phoneNo;
    }


}