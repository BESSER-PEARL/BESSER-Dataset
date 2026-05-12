





import java.util.List;
import java.util.ArrayList;

public class Costomer  {

    private String Address;
    private String Name;
    private String Email;
    private int ID;
    private int mobileNumber;



    public Costomer(
        String Address,        String Name,        String Email,        int ID,        int mobileNumber    ) {
        this.Address = Address;
        this.Name = Name;
        this.Email = Email;
        this.ID = ID;
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
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getMobilenumber() {
        return mobileNumber;
    }

    public void setMobilenumber(int mobileNumber) {
        this.mobileNumber = mobileNumber;
    }


}