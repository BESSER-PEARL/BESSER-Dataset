





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String User_Id;
    private String User_contact;
    private String User_Address;
    private String User_Name;
    private String User_Email;
    private String User_DOB;



    public User(
        String User_Id,        String User_contact,        String User_Address,        String User_Name,        String User_Email,        String User_DOB    ) {
        this.User_Id = User_Id;
        this.User_contact = User_contact;
        this.User_Address = User_Address;
        this.User_Name = User_Name;
        this.User_Email = User_Email;
        this.User_DOB = User_DOB;
    }


    public String getUser_id() {
        return User_Id;
    }

    public void setUser_id(String User_Id) {
        this.User_Id = User_Id;
    }
    public String getUser_contact() {
        return User_contact;
    }

    public void setUser_contact(String User_contact) {
        this.User_contact = User_contact;
    }
    public String getUser_address() {
        return User_Address;
    }

    public void setUser_address(String User_Address) {
        this.User_Address = User_Address;
    }
    public String getUser_name() {
        return User_Name;
    }

    public void setUser_name(String User_Name) {
        this.User_Name = User_Name;
    }
    public String getUser_email() {
        return User_Email;
    }

    public void setUser_email(String User_Email) {
        this.User_Email = User_Email;
    }
    public String getUser_dob() {
        return User_DOB;
    }

    public void setUser_dob(String User_DOB) {
        this.User_DOB = User_DOB;
    }


}