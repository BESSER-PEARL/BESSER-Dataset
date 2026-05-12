





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String UserName;
    private int Phone;
    private String Password;
    private int Point;
    private int ID;
    private String UserInfo;
    private String Email;



    public User(
        String UserName,        int Phone,        String Password,        int Point,        int ID,        String UserInfo,        String Email    ) {
        this.UserName = UserName;
        this.Phone = Phone;
        this.Password = Password;
        this.Point = Point;
        this.ID = ID;
        this.UserInfo = UserInfo;
        this.Email = Email;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getPoint() {
        return Point;
    }

    public void setPoint(int Point) {
        this.Point = Point;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getUserinfo() {
        return UserInfo;
    }

    public void setUserinfo(String UserInfo) {
        this.UserInfo = UserInfo;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}