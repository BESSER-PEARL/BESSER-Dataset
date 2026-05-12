





import java.util.List;
import java.util.ArrayList;

public class SuperAdmin  {

    private String password;
    private int adminID;





    private DataBase database;


    public SuperAdmin(
        String password,        int adminID    ) {
        this.password = password;
        this.adminID = adminID;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getAdminid() {
        return adminID;
    }

    public void setAdminid(int adminID) {
        this.adminID = adminID;
    }

    public DataBase getDatabase() {
        return database;
    }

    public void setDatabase(DataBase database) {
        this.database = database;
    }

}