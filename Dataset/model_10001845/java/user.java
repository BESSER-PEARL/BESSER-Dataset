





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String sex;
    private String user_name;
    private String pas;



    public user(
        String sex,        String user_name,        String pas    ) {
        this.sex = sex;
        this.user_name = user_name;
        this.pas = pas;
    }


    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getUser_name() {
        return user_name;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }
    public String getPas() {
        return pas;
    }

    public void setPas(String pas) {
        this.pas = pas;
    }


}