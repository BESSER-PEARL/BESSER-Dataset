





import java.util.List;
import java.util.ArrayList;

public class esmodel_url_ServerUrl  {

    private int port;
    private String hostName;



    public esmodel_url_ServerUrl(
        int port,        String hostName    ) {
        this.port = port;
        this.hostName = hostName;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getHostname() {
        return hostName;
    }

    public void setHostname(String hostName) {
        this.hostName = hostName;
    }


}