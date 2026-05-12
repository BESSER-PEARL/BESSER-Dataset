





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private None instance;
    private String url;
    private String username;
    private String password;



    public Database(
        None instance,        String url,        String username,        String password    ) {
        this.instance = instance;
        this.url = url;
        this.username = username;
        this.password = password;
    }


    public None getInstance() {
        return instance;
    }

    public void setInstance(None instance) {
        this.instance = instance;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}