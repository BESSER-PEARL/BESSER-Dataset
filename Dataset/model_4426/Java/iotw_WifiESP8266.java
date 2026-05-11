





import java.util.List;
import java.util.ArrayList;

public class iotw_WifiESP8266 extends Connectivity {

    private String sSID_AccessPoint;
    private String idConnection;
    private String baud;
    private String connectedChannel;
    private String pinVcc;
    private String sSID_ST;
    private String pinGND;
    private String password_ST;
    private String pinRX;
    private int port;
    private String mode;
    private String pinCHPD;
    private String iP;
    private String protocol;
    private String pinTX;
    private String password_AccessPoint;



    public iotw_WifiESP8266(
        String sSID_AccessPoint,        String idConnection,        String baud,        String connectedChannel,        String pinVcc,        String sSID_ST,        String pinGND,        String password_ST,        String pinRX,        int port,        String mode,        String pinCHPD,        String iP,        String protocol,        String pinTX,        String password_AccessPoint    ) {
        super(
        );
        this.sSID_AccessPoint = sSID_AccessPoint;
        this.idConnection = idConnection;
        this.baud = baud;
        this.connectedChannel = connectedChannel;
        this.pinVcc = pinVcc;
        this.sSID_ST = sSID_ST;
        this.pinGND = pinGND;
        this.password_ST = password_ST;
        this.pinRX = pinRX;
        this.port = port;
        this.mode = mode;
        this.pinCHPD = pinCHPD;
        this.iP = iP;
        this.protocol = protocol;
        this.pinTX = pinTX;
        this.password_AccessPoint = password_AccessPoint;
    }


    public String getSsid_accesspoint() {
        return sSID_AccessPoint;
    }

    public void setSsid_accesspoint(String sSID_AccessPoint) {
        this.sSID_AccessPoint = sSID_AccessPoint;
    }
    public String getIdconnection() {
        return idConnection;
    }

    public void setIdconnection(String idConnection) {
        this.idConnection = idConnection;
    }
    public String getBaud() {
        return baud;
    }

    public void setBaud(String baud) {
        this.baud = baud;
    }
    public String getConnectedchannel() {
        return connectedChannel;
    }

    public void setConnectedchannel(String connectedChannel) {
        this.connectedChannel = connectedChannel;
    }
    public String getPinvcc() {
        return pinVcc;
    }

    public void setPinvcc(String pinVcc) {
        this.pinVcc = pinVcc;
    }
    public String getSsid_st() {
        return sSID_ST;
    }

    public void setSsid_st(String sSID_ST) {
        this.sSID_ST = sSID_ST;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPassword_st() {
        return password_ST;
    }

    public void setPassword_st(String password_ST) {
        this.password_ST = password_ST;
    }
    public String getPinrx() {
        return pinRX;
    }

    public void setPinrx(String pinRX) {
        this.pinRX = pinRX;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getPinchpd() {
        return pinCHPD;
    }

    public void setPinchpd(String pinCHPD) {
        this.pinCHPD = pinCHPD;
    }
    public String getIp() {
        return iP;
    }

    public void setIp(String iP) {
        this.iP = iP;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getPintx() {
        return pinTX;
    }

    public void setPintx(String pinTX) {
        this.pinTX = pinTX;
    }
    public String getPassword_accesspoint() {
        return password_AccessPoint;
    }

    public void setPassword_accesspoint(String password_AccessPoint) {
        this.password_AccessPoint = password_AccessPoint;
    }


}