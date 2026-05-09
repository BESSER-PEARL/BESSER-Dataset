





import java.util.List;
import java.util.ArrayList;

public class esmodel_url_ServerUrl  {

    private String hostName;
    private int port;



    public esmodel_url_ServerUrl(
        String hostName,        int port    ) {
        this.hostName = hostName;
        this.port = port;
    }


    public String getHostname() {
        return hostName;
    }

    public void setHostname(String hostName) {
        this.hostName = hostName;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }


}