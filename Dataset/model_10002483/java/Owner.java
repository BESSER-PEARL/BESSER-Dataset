





import java.util.List;
import java.util.ArrayList;

public class Owner  {

    private String Name;
    private None Phn_no_;
    private String Address;
    private int ID;
    private int password;
    private int email_id;



    public Owner(
        String Name,        None Phn_no_,        String Address,        int ID,        int password,        int email_id    ) {
        this.Name = Name;
        this.Phn_no_ = Phn_no_;
        this.Address = Address;
        this.ID = ID;
        this.password = password;
        this.email_id = email_id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public None getPhn_no_() {
        return Phn_no_;
    }

    public void setPhn_no_(None Phn_no_) {
        this.Phn_no_ = Phn_no_;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public int getEmail_id() {
        return email_id;
    }

    public void setEmail_id(int email_id) {
        this.email_id = email_id;
    }


}