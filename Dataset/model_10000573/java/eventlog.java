





import java.util.List;
import java.util.ArrayList;

public class eventlog  {

    private int event_id;
    private int event_time;
    private String event_info;





    private login login;


    public eventlog(
        int event_id,        int event_time,        String event_info    ) {
        this.event_id = event_id;
        this.event_time = event_time;
        this.event_info = event_info;
    }


    public int getEvent_id() {
        return event_id;
    }

    public void setEvent_id(int event_id) {
        this.event_id = event_id;
    }
    public int getEvent_time() {
        return event_time;
    }

    public void setEvent_time(int event_time) {
        this.event_time = event_time;
    }
    public String getEvent_info() {
        return event_info;
    }

    public void setEvent_info(String event_info) {
        this.event_info = event_info;
    }

    public login getLogin() {
        return login;
    }

    public void setLogin(login login) {
        this.login = login;
    }

}