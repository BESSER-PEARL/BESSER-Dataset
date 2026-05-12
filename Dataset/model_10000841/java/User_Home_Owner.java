





import java.util.List;
import java.util.ArrayList;

public class User_Home_Owner  {

    private int UserID;





    private Alert alert;


    public User_Home_Owner(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public Alert getAlert() {
        return alert;
    }

    public void setAlert(Alert alert) {
        this.alert = alert;
    }

}