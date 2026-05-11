





import java.util.List;
import java.util.ArrayList;

public class selflet_Reds  {

    private String ipAddress;
    private String port;



    public selflet_Reds(
        String ipAddress,        String port    ) {
        this.ipAddress = ipAddress;
        this.port = port;
    }


    public String getIpaddress() {
        return ipAddress;
    }

    public void setIpaddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }


}