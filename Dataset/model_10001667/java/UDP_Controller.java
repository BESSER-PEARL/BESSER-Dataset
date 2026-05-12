





import java.util.List;
import java.util.ArrayList;

public class UDP_Controller  {

    private String ip_session;



    public UDP_Controller(
        String ip_session    ) {
        this.ip_session = ip_session;
    }


    public String getIp_session() {
        return ip_session;
    }

    public void setIp_session(String ip_session) {
        this.ip_session = ip_session;
    }


}