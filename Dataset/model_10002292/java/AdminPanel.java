





import java.util.List;
import java.util.ArrayList;

public class AdminPanel  {

    private int UserLevel;
    private int UserID;
    private String UserName;





    private Menu menu;


    public AdminPanel(
        int UserLevel,        int UserID,        String UserName    ) {
        this.UserLevel = UserLevel;
        this.UserID = UserID;
        this.UserName = UserName;
    }


    public int getUserlevel() {
        return UserLevel;
    }

    public void setUserlevel(int UserLevel) {
        this.UserLevel = UserLevel;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }

    public Menu getMenu() {
        return menu;
    }

    public void setMenu(Menu menu) {
        this.menu = menu;
    }

}