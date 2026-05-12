





import java.util.List;
import java.util.ArrayList;

public class user  {

    private int id_user;
    private String password;
    private String username;
    private String nama_user;



    public user(
        int id_user,        String password,        String username,        String nama_user    ) {
        this.id_user = id_user;
        this.password = password;
        this.username = username;
        this.nama_user = nama_user;
    }


    public int getId_user() {
        return id_user;
    }

    public void setId_user(int id_user) {
        this.id_user = id_user;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getNama_user() {
        return nama_user;
    }

    public void setNama_user(String nama_user) {
        this.nama_user = nama_user;
    }


}