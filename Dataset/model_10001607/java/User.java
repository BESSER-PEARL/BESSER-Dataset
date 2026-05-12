





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String loginStatus;
    private String nama;
    private String password;
    private String userName;



    public User(
        String loginStatus,        String nama,        String password,        String userName    ) {
        this.loginStatus = loginStatus;
        this.nama = nama;
        this.password = password;
        this.userName = userName;
    }


    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
    }
    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }


}