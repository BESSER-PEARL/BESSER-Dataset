





import java.util.List;
import java.util.ArrayList;

public class Users1  {

    private String id;
    private String password;



    public Users1(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}