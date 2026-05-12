





import java.util.List;
import java.util.ArrayList;

public class UserAdmin  {

    private int adminID;
    private String password;





    private DataBase database;


    public UserAdmin(
        int adminID,        String password    ) {
        this.adminID = adminID;
        this.password = password;
    }


    public int getAdminid() {
        return adminID;
    }

    public void setAdminid(int adminID) {
        this.adminID = adminID;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public DataBase getDatabase() {
        return database;
    }

    public void setDatabase(DataBase database) {
        this.database = database;
    }

}