





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String Name;
    private String attribute;
    private String password;
    private String email;
    private String _attr;
    private String id;



    public Account(
        String Name,        String attribute,        String password,        String email,        String _attr,        String id    ) {
        this.Name = Name;
        this.attribute = attribute;
        this.password = password;
        this.email = email;
        this._attr = _attr;
        this.id = id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}