





import java.util.List;
import java.util.ArrayList;

public class Costomer  {

    private String Name;
    private int mobileNumber;
    private int ID;
    private String Address;
    private String Email;



    public Costomer(
        String Name,        int mobileNumber,        int ID,        String Address,        String Email    ) {
        this.Name = Name;
        this.mobileNumber = mobileNumber;
        this.ID = ID;
        this.Address = Address;
        this.Email = Email;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getMobilenumber() {
        return mobileNumber;
    }

    public void setMobilenumber(int mobileNumber) {
        this.mobileNumber = mobileNumber;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}