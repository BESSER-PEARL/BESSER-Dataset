





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__App_User  {

    private String passwd;
    private String login_id;



    public NO_Queue_mobile_application__App_User(
        String passwd,        String login_id    ) {
        this.passwd = passwd;
        this.login_id = login_id;
    }


    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }
    public String getLogin_id() {
        return login_id;
    }

    public void setLogin_id(String login_id) {
        this.login_id = login_id;
    }


}