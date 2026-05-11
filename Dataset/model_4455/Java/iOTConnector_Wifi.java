





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_Wifi  {

    private String ssid;
    private String password;





    private iOTConnector_Program iotconnector_program;


    public iOTConnector_Wifi(
        String ssid,        String password    ) {
        this.ssid = ssid;
        this.password = password;
    }


    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public iOTConnector_Program getIotconnector_program() {
        return iotconnector_program;
    }

    public void setIotconnector_program(iOTConnector_Program iotconnector_program) {
        this.iotconnector_program = iotconnector_program;
    }

}