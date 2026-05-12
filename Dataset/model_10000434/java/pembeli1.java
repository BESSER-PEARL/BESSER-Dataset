





import java.util.List;
import java.util.ArrayList;

public class pembeli1  {

    private int id_role;
    private String username;
    private String mail;
    private String address;
    private String name;
    private int id;
    private String password;





    private user user;


    public pembeli1(
        int id_role,        String username,        String mail,        String address,        String name,        int id,        String password    ) {
        this.id_role = id_role;
        this.username = username;
        this.mail = mail;
        this.address = address;
        this.name = name;
        this.id = id;
        this.password = password;
    }


    public int getId_role() {
        return id_role;
    }

    public void setId_role(int id_role) {
        this.id_role = id_role;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}