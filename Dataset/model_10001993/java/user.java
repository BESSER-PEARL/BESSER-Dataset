





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String email;
    private String password;
    private String id_user;
    private String nama_user;



    public user(
        String email,        String password,        String id_user,        String nama_user    ) {
        this.email = email;
        this.password = password;
        this.id_user = id_user;
        this.nama_user = nama_user;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId_user() {
        return id_user;
    }

    public void setId_user(String id_user) {
        this.id_user = id_user;
    }
    public String getNama_user() {
        return nama_user;
    }

    public void setNama_user(String nama_user) {
        this.nama_user = nama_user;
    }


}