





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String RegisterDate;
    private String Username;
    private String UserID;
    private boolean isActive;
    private int RoleID;
    private String Password;





    private OnlineShop onlineshop;


    public User(
        String RegisterDate,        String Username,        String UserID,        boolean isActive,        int RoleID,        String Password    ) {
        this.RegisterDate = RegisterDate;
        this.Username = Username;
        this.UserID = UserID;
        this.isActive = isActive;
        this.RoleID = RoleID;
        this.Password = Password;
    }


    public String getRegisterdate() {
        return RegisterDate;
    }

    public void setRegisterdate(String RegisterDate) {
        this.RegisterDate = RegisterDate;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getUserid() {
        return UserID;
    }

    public void setUserid(String UserID) {
        this.UserID = UserID;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public int getRoleid() {
        return RoleID;
    }

    public void setRoleid(int RoleID) {
        this.RoleID = RoleID;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public OnlineShop getOnlineshop() {
        return onlineshop;
    }

    public void setOnlineshop(OnlineShop onlineshop) {
        this.onlineshop = onlineshop;
    }

}