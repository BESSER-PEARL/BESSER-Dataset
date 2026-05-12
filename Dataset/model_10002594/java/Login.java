





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String username;
    private String _attr;



    public Login(
        String username,        String _attr    ) {
        this.username = username;
        this._attr = _attr;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }


}