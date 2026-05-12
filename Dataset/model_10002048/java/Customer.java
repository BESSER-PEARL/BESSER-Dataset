





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Name;
    private String Address;
    private String ContactNo;
    private String Email;
    private int CusID;



    public Customer(
        String Name,        String Address,        String ContactNo,        String Email,        int CusID    ) {
        this.Name = Name;
        this.Address = Address;
        this.ContactNo = ContactNo;
        this.Email = Email;
        this.CusID = CusID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getContactno() {
        return ContactNo;
    }

    public void setContactno(String ContactNo) {
        this.ContactNo = ContactNo;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getCusid() {
        return CusID;
    }

    public void setCusid(int CusID) {
        this.CusID = CusID;
    }


}