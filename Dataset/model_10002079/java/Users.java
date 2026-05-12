





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String Password;
    private int RegisterDate;
    private String UserID;
    private String LoginStatus;



    public Users(
        String Password,        int RegisterDate,        String UserID,        String LoginStatus    ) {
        this.Password = Password;
        this.RegisterDate = RegisterDate;
        this.UserID = UserID;
        this.LoginStatus = LoginStatus;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getRegisterdate() {
        return RegisterDate;
    }

    public void setRegisterdate(int RegisterDate) {
        this.RegisterDate = RegisterDate;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public String getLoginstatus() {
        return LoginStatus;
    }

    public void setLoginstatus(String LoginStatus) {
        this.LoginStatus = LoginStatus;
    }


}