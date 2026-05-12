





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String insertData;
    private String attribute;
    private String username;
    private String password;
    private int ID_admin;



    public Admin(
        String insertData,        String attribute,        String username,        String password,        int ID_admin    ) {
        this.insertData = insertData;
        this.attribute = attribute;
        this.username = username;
        this.password = password;
        this.ID_admin = ID_admin;
    }


    public String getInsertdata() {
        return insertData;
    }

    public void setInsertdata(String insertData) {
        this.insertData = insertData;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getId_admin() {
        return ID_admin;
    }

    public void setId_admin(int ID_admin) {
        this.ID_admin = ID_admin;
    }


}