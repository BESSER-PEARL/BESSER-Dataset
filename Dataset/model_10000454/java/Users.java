





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String UserID;
    private String LoginStatus;
    private String Password;
    private int RegisterDate;



    public Users(
        String UserID,        String LoginStatus,        String Password,        int RegisterDate    ) {
        this.UserID = UserID;
        this.LoginStatus = LoginStatus;
        this.Password = Password;
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


}