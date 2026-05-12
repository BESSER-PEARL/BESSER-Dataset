





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;
    private String password;
    private String family;
    private int uid;
    private String userName;



    public User(
        String name,        String password,        String family,        int uid,        String userName    ) {
        this.name = name;
        this.password = password;
        this.family = family;
        this.uid = uid;
        this.userName = userName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
    public int getUid() {
        return uid;
    }

    public void setUid(int uid) {
        this.uid = uid;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }


}