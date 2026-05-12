





import java.util.List;
import java.util.ArrayList;

public class admin  {

    private int user_type;
    private String user_name;
    private int user_mobile;



    public admin(
        int user_type,        String user_name,        int user_mobile    ) {
        this.user_type = user_type;
        this.user_name = user_name;
        this.user_mobile = user_mobile;
    }


    public int getUser_type() {
        return user_type;
    }

    public void setUser_type(int user_type) {
        this.user_type = user_type;
    }
    public String getUser_name() {
        return user_name;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }
    public int getUser_mobile() {
        return user_mobile;
    }

    public void setUser_mobile(int user_mobile) {
        this.user_mobile = user_mobile;
    }


}