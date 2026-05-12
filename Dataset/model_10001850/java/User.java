





import java.util.List;
import java.util.ArrayList;

public class User  {

    private None View_Account_Purchase_History__;
    private String loginStatus;
    private String userId;
    private String password;
    private None Update_Account_Information__;
    private None Logout__;



    public User(
        None View_Account_Purchase_History__,        String loginStatus,        String userId,        String password,        None Update_Account_Information__,        None Logout__    ) {
        this.View_Account_Purchase_History__ = View_Account_Purchase_History__;
        this.loginStatus = loginStatus;
        this.userId = userId;
        this.password = password;
        this.Update_Account_Information__ = Update_Account_Information__;
        this.Logout__ = Logout__;
    }


    public None getView_account_purchase_history__() {
        return View_Account_Purchase_History__;
    }

    public void setView_account_purchase_history__(None View_Account_Purchase_History__) {
        this.View_Account_Purchase_History__ = View_Account_Purchase_History__;
    }
    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public None getUpdate_account_information__() {
        return Update_Account_Information__;
    }

    public void setUpdate_account_information__(None Update_Account_Information__) {
        this.Update_Account_Information__ = Update_Account_Information__;
    }
    public None getLogout__() {
        return Logout__;
    }

    public void setLogout__(None Logout__) {
        this.Logout__ = Logout__;
    }


}