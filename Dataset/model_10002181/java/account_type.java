





import java.util.List;
import java.util.ArrayList;

public class account_type  {

    private String password;
    private String id;
    private String name;
    private String email;
    private String _attr;



    public account_type(
        String password,        String id,        String name,        String email,        String _attr    ) {
        this.password = password;
        this.id = id;
        this.name = name;
        this.email = email;
        this._attr = _attr;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }


}