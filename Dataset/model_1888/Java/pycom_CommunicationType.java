





import java.util.List;
import java.util.ArrayList;

public class pycom_CommunicationType  {

    private String password;
    private String ssid;
    private String name;





    private pycom_Communication pycom_communication;


    public pycom_CommunicationType(
        String password,        String ssid,        String name    ) {
        this.password = password;
        this.ssid = ssid;
        this.name = name;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pycom_Communication getPycom_communication() {
        return pycom_communication;
    }

    public void setPycom_communication(pycom_Communication pycom_communication) {
        this.pycom_communication = pycom_communication;
    }

}