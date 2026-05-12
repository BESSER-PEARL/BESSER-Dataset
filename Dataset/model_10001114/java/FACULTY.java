





import java.util.List;
import java.util.ArrayList;

public class FACULTY  {

    private String id;
    private String password;



    public FACULTY(
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