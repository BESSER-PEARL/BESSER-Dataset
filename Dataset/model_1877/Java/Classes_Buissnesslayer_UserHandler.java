





import java.util.List;
import java.util.ArrayList;

public class Classes_Buissnesslayer_UserHandler  {

    private String Users;





    private Database database;




    private LoginController logincontroller;


    public Classes_Buissnesslayer_UserHandler(
        String Users    ) {
        this.Users = Users;
    }


    public String getUsers() {
        return Users;
    }

    public void setUsers(String Users) {
        this.Users = Users;
    }

    public Database getDatabase() {
        return database;
    }

    public void setDatabase(Database database) {
        this.database = database;
    }
    public LoginController getLogincontroller() {
        return logincontroller;
    }

    public void setLogincontroller(LoginController logincontroller) {
        this.logincontroller = logincontroller;
    }

}