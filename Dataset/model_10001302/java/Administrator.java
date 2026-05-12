





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String email;
    private int user_id;
    private String user_name;



    public Administrator(
        String email,        int user_id,        String user_name    ) {
        this.email = email;
        this.user_id = user_id;
        this.user_name = user_name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public String getUser_name() {
        return user_name;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }


}