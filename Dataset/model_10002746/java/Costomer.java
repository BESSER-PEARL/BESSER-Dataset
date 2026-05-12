





import java.util.List;
import java.util.ArrayList;

public class Costomer  {

    private String Email;
    private int mobileNumber;
    private int ID;
    private String Name;
    private String Address;



    public Costomer(
        String Email,        int mobileNumber,        int ID,        String Name,        String Address    ) {
        this.Email = Email;
        this.mobileNumber = mobileNumber;
        this.ID = ID;
        this.Name = Name;
        this.Address = Address;
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
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
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


}