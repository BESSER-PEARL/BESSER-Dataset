





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_Webserver  {

    private int port;
    private String url;



    public iOTConnector_Webserver(
        int port,        String url    ) {
        this.port = port;
        this.url = url;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}