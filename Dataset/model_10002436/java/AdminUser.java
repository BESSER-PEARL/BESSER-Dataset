





import java.util.List;
import java.util.ArrayList;

public class AdminUser  {

    private String email;
    private boolean active;
    private String roles;
    private String password;
    private String id;
    private String phone;
    private String username;



    public AdminUser(
        String email,        boolean active,        String roles,        String password,        String id,        String phone,        String username    ) {
        this.email = email;
        this.active = active;
        this.roles = roles;
        this.password = password;
        this.id = id;
        this.phone = phone;
        this.username = username;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getRoles() {
        return roles;
    }

    public void setRoles(String roles) {
        this.roles = roles;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}