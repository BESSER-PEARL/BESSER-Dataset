





import java.util.List;
import java.util.ArrayList;

public class selflet_Reds  {

    private String port;
    private String ipAddress;





    private selflet_SelfletProperties selflet_selfletproperties;


    public selflet_Reds(
        String port,        String ipAddress    ) {
        this.port = port;
        this.ipAddress = ipAddress;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getIpaddress() {
        return ipAddress;
    }

    public void setIpaddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    public selflet_SelfletProperties getSelflet_selfletproperties() {
        return selflet_selfletproperties;
    }

    public void setSelflet_selfletproperties(selflet_SelfletProperties selflet_selfletproperties) {
        this.selflet_selfletproperties = selflet_selfletproperties;
    }

}