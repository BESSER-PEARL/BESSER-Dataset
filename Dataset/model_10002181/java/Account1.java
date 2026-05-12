





import java.util.List;
import java.util.ArrayList;

public class Account1  {

    private String password;
    private String attribute;
    private String Name;
    private String email;
    private String id;
    private String _attr;



    public Account1(
        String password,        String attribute,        String Name,        String email,        String id,        String _attr    ) {
        this.password = password;
        this.attribute = attribute;
        this.Name = Name;
        this.email = email;
        this.id = id;
        this._attr = _attr;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }


}