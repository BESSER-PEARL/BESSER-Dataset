





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Gender;
    private int Mobile;
    private int Zipcode;
    private String State;
    private String Address;
    private int CustId;
    private String Lname;
    private String FName;
    private String attribute;
    private String DOB;



    public Customer(
        String Gender,        int Mobile,        int Zipcode,        String State,        String Address,        int CustId,        String Lname,        String FName,        String attribute,        String DOB    ) {
        this.Gender = Gender;
        this.Mobile = Mobile;
        this.Zipcode = Zipcode;
        this.State = State;
        this.Address = Address;
        this.CustId = CustId;
        this.Lname = Lname;
        this.FName = FName;
        this.attribute = attribute;
        this.DOB = DOB;
    }


    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public int getMobile() {
        return Mobile;
    }

    public void setMobile(int Mobile) {
        this.Mobile = Mobile;
    }
    public int getZipcode() {
        return Zipcode;
    }

    public void setZipcode(int Zipcode) {
        this.Zipcode = Zipcode;
    }
    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getCustid() {
        return CustId;
    }

    public void setCustid(int CustId) {
        this.CustId = CustId;
    }
    public String getLname() {
        return Lname;
    }

    public void setLname(String Lname) {
        this.Lname = Lname;
    }
    public String getFname() {
        return FName;
    }

    public void setFname(String FName) {
        this.FName = FName;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }


}