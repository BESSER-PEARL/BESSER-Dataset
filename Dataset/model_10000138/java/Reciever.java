





import java.util.List;
import java.util.ArrayList;

public class Reciever  {

    private int id;
    private boolean is_private;
    private int user_id;
    private boolean is_admin;
    private String surname;
    private String mail;
    private String password;
    private String username;
    private String name;
    private String phone;
    private boolean is_active;



    public Reciever(
        int id,        boolean is_private,        int user_id,        boolean is_admin,        String surname,        String mail,        String password,        String username,        String name,        String phone,        boolean is_active    ) {
        this.id = id;
        this.is_private = is_private;
        this.user_id = user_id;
        this.is_admin = is_admin;
        this.surname = surname;
        this.mail = mail;
        this.password = password;
        this.username = username;
        this.name = name;
        this.phone = phone;
        this.is_active = is_active;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getIs_private() {
        return is_private;
    }

    public void setIs_private(boolean is_private) {
        this.is_private = is_private;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public boolean getIs_admin() {
        return is_admin;
    }

    public void setIs_admin(boolean is_admin) {
        this.is_admin = is_admin;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public boolean getIs_active() {
        return is_active;
    }

    public void setIs_active(boolean is_active) {
        this.is_active = is_active;
    }


}