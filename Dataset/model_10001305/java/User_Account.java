





import java.util.List;
import java.util.ArrayList;

public class User_Account  {

    private String FullName;
    private String RegDate;
    private String UserAddress;
    private String UserID;
    private String Email;
    private String DateOfBirth;



    public User_Account(
        String FullName,        String RegDate,        String UserAddress,        String UserID,        String Email,        String DateOfBirth    ) {
        this.FullName = FullName;
        this.RegDate = RegDate;
        this.UserAddress = UserAddress;
        this.UserID = UserID;
        this.Email = Email;
        this.DateOfBirth = DateOfBirth;
    }


    public String getFullname() {
        return FullName;
    }

    public void setFullname(String FullName) {
        this.FullName = FullName;
    }
    public String getRegdate() {
        return RegDate;
    }

    public void setRegdate(String RegDate) {
        this.RegDate = RegDate;
    }
    public String getUseraddress() {
        return UserAddress;
    }

    public void setUseraddress(String UserAddress) {
        this.UserAddress = UserAddress;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDateofbirth() {
        return DateOfBirth;
    }

    public void setDateofbirth(String DateOfBirth) {
        this.DateOfBirth = DateOfBirth;
    }


}