





import java.util.List;
import java.util.ArrayList;

public class iotw_WifiESP8266 extends Connectivity {

    private String iP;
    private String password_AccessPoint;
    private String sSID_AccessPoint;
    private String password_ST;
    private String connectedChannel;
    private int port;
    private String pinGND;
    private String pinTX;
    private String pinCHPD;
    private String mode;
    private String protocol;
    private String pinRX;
    private String pinVcc;
    private String sSID_ST;
    private String idConnection;
    private String baud;



    public iotw_WifiESP8266(
        String iP,        String password_AccessPoint,        String sSID_AccessPoint,        String password_ST,        String connectedChannel,        int port,        String pinGND,        String pinTX,        String pinCHPD,        String mode,        String protocol,        String pinRX,        String pinVcc,        String sSID_ST,        String idConnection,        String baud    ) {
        super(
        );
        this.iP = iP;
        this.password_AccessPoint = password_AccessPoint;
        this.sSID_AccessPoint = sSID_AccessPoint;
        this.password_ST = password_ST;
        this.connectedChannel = connectedChannel;
        this.port = port;
        this.pinGND = pinGND;
        this.pinTX = pinTX;
        this.pinCHPD = pinCHPD;
        this.mode = mode;
        this.protocol = protocol;
        this.pinRX = pinRX;
        this.pinVcc = pinVcc;
        this.sSID_ST = sSID_ST;
        this.idConnection = idConnection;
        this.baud = baud;
    }


    public String getIp() {
        return iP;
    }

    public void setIp(String iP) {
        this.iP = iP;
    }
    public String getPassword_accesspoint() {
        return password_AccessPoint;
    }

    public void setPassword_accesspoint(String password_AccessPoint) {
        this.password_AccessPoint = password_AccessPoint;
    }
    public String getSsid_accesspoint() {
        return sSID_AccessPoint;
    }

    public void setSsid_accesspoint(String sSID_AccessPoint) {
        this.sSID_AccessPoint = sSID_AccessPoint;
    }
    public String getPassword_st() {
        return password_ST;
    }

    public void setPassword_st(String password_ST) {
        this.password_ST = password_ST;
    }
    public String getConnectedchannel() {
        return connectedChannel;
    }

    public void setConnectedchannel(String connectedChannel) {
        this.connectedChannel = connectedChannel;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getPingnd() {
        return pinGND;
    }

    public void setPingnd(String pinGND) {
        this.pinGND = pinGND;
    }
    public String getPintx() {
        return pinTX;
    }

    public void setPintx(String pinTX) {
        this.pinTX = pinTX;
    }
    public String getPinchpd() {
        return pinCHPD;
    }

    public void setPinchpd(String pinCHPD) {
        this.pinCHPD = pinCHPD;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }
    public String getPinrx() {
        return pinRX;
    }

    public void setPinrx(String pinRX) {
        this.pinRX = pinRX;
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


}