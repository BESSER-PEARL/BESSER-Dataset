





import java.util.List;
import java.util.ArrayList;

public class pembeli1  {

    private String username;
    private String address;
    private String mail;
    private String password;
    private String name;
    private int id;
    private int id_role;





    private user user;


    public pembeli1(
        String username,        String address,        String mail,        String password,        String name,        int id,        int id_role    ) {
        this.username = username;
        this.address = address;
        this.mail = mail;
        this.password = password;
        this.name = name;
        this.id = id;
        this.id_role = id_role;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getId_role() {
        return id_role;
    }

    public void setId_role(int id_role) {
        this.id_role = id_role;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}