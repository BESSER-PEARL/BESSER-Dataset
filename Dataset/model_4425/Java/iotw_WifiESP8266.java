





import java.util.List;
import java.util.ArrayList;

public class iotw_WifiESP8266 extends ConnectivityControl {

    private String pinCHPD;
    private String pinRX;
    private String pinTX;
    private String Password;
    private String Host;
    private int Port;
    private String SSID;
    private String pinGND;
    private String pinVcc;



    public iotw_WifiESP8266(
        String pinCHPD,        String pinRX,        String pinTX,        String Password,        String Host,        int Port,        String SSID,        String pinGND,        String pinVcc    ) {
        super(
        );
        this.pinCHPD = pinCHPD;
        this.pinRX = pinRX;
        this.pinTX = pinTX;
        this.Password = Password;
        this.Host = Host;
        this.Port = Port;
        this.SSID = SSID;
        this.pinGND = pinGND;
        this.pinVcc = pinVcc;
    }


    public String getPinchpd() {
        return pinCHPD;
    }

    public void setPinchpd(String pinCHPD) {
        this.pinCHPD = pinCHPD;
    }
    public String getPinrx() {
        return pinRX;
    }

    public void setPinrx(String pinRX) {
        this.pinRX = pinRX;
    }
    public String getPintx() {
        return pinTX;
    }

    public void setPintx(String pinTX) {
        this.pinTX = pinTX;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public int getPort() {
        return Port;
    }

    public void setPort(int Port) {
        this.Port = Port;
    }
    public String getSsid() {
        return SSID;
    }

    public void setSsid(String SSID) {
        this.SSID = SSID;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPinvcc() {
        return pinVcc;
    }

    public void setPinvcc(String pinVcc) {
        this.pinVcc = pinVcc;
    }


}