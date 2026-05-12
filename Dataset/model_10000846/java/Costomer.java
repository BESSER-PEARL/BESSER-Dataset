





import java.util.List;
import java.util.ArrayList;

public class Costomer  {

    private String Email;
    private int mobileNumber;
    private String Address;
    private String Name;
    private int ID;



    public Costomer(
        String Email,        int mobileNumber,        String Address,        String Name,        int ID    ) {
        this.Email = Email;
        this.mobileNumber = mobileNumber;
        this.Address = Address;
        this.Name = Name;
        this.ID = ID;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getMobilenumber() {
        return mobileNumber;
    }

    public void setMobilenumber(int mobileNumber) {
        this.mobileNumber = mobileNumber;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}