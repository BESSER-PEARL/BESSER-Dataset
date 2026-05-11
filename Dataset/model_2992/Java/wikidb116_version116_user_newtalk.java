





import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_user_newtalk  {

    private String user_ip;
    private String user_id;
    private String user_last_timestamp;



    public wikidb116_version116_user_newtalk(
        String user_ip,        String user_id,        String user_last_timestamp    ) {
        this.user_ip = user_ip;
        this.user_id = user_id;
        this.user_last_timestamp = user_last_timestamp;
    }


    public String getUser_ip() {
        return user_ip;
    }

    public void setUser_ip(String user_ip) {
        this.user_ip = user_ip;
    }
    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getUser_last_timestamp() {
        return user_last_timestamp;
    }

    public void setUser_last_timestamp(String user_last_timestamp) {
        this.user_last_timestamp = user_last_timestamp;
    }


}