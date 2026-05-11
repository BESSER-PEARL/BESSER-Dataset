





import java.util.List;
import java.util.ArrayList;

public class iotw_ArduinoWiFiESP8266WeMosD1 extends Mainboard {

    private String wifiMode;
    private String gateway;
    private String dns;
    private String ssid;
    private int baud;
    private String password;
    private String ip;
    private String pinD7;
    private String pinD6;
    private String pinD8;
    private String pinD4;
    private String pinD2;
    private String pinD0;
    private String subnet;
    private String pinSDA;
    private String pinSCL;
    private String pinD1;
    private String pinA0;
    private String pinD3;
    private String pinD5;



    public iotw_ArduinoWiFiESP8266WeMosD1(
        String wifiMode,        String gateway,        String dns,        String ssid,        int baud,        String password,        String ip,        String pinD7,        String pinD6,        String pinD8,        String pinD4,        String pinD2,        String pinD0,        String subnet,        String pinSDA,        String pinSCL,        String pinD1,        String pinA0,        String pinD3,        String pinD5    ) {
        super(
        );
        this.wifiMode = wifiMode;
        this.gateway = gateway;
        this.dns = dns;
        this.ssid = ssid;
        this.baud = baud;
        this.password = password;
        this.ip = ip;
        this.pinD7 = pinD7;
        this.pinD6 = pinD6;
        this.pinD8 = pinD8;
        this.pinD4 = pinD4;
        this.pinD2 = pinD2;
        this.pinD0 = pinD0;
        this.subnet = subnet;
        this.pinSDA = pinSDA;
        this.pinSCL = pinSCL;
        this.pinD1 = pinD1;
        this.pinA0 = pinA0;
        this.pinD3 = pinD3;
        this.pinD5 = pinD5;
    }


    public String getWifimode() {
        return wifiMode;
    }

    public void setWifimode(String wifiMode) {
        this.wifiMode = wifiMode;
    }
    public String getGateway() {
        return gateway;
    }

    public void setGateway(String gateway) {
        this.gateway = gateway;
    }
    public String getDns() {
        return dns;
    }

    public void setDns(String dns) {
        this.dns = dns;
    }
    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public int getBaud() {
        return baud;
    }

    public void setBaud(int baud) {
        this.baud = baud;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }
    public String getPind7() {
        return pinD7;
    }

    public void setPind7(String pinD7) {
        this.pinD7 = pinD7;
    }
    public String getPind6() {
        return pinD6;
    }

    public void setPind6(String pinD6) {
        this.pinD6 = pinD6;
    }
    public String getPind8() {
        return pinD8;
    }

    public void setPind8(String pinD8) {
        this.pinD8 = pinD8;
    }
    public String getPind4() {
        return pinD4;
    }

    public void setPind4(String pinD4) {
        this.pinD4 = pinD4;
    }
    public String getPind2() {
        return pinD2;
    }

    public void setPind2(String pinD2) {
        this.pinD2 = pinD2;
    }
    public String getPind0() {
        return pinD0;
    }

    public void setPind0(String pinD0) {
        this.pinD0 = pinD0;
    }
    public String getSubnet() {
        return subnet;
    }

    public void setSubnet(String subnet) {
        this.subnet = subnet;
    }
    public String getPinsda() {
        return pinSDA;
    }

    public void setPinsda(String pinSDA) {
        this.pinSDA = pinSDA;
    }
    public String getPinscl() {
        return pinSCL;
    }

    public void setPinscl(String pinSCL) {
        this.pinSCL = pinSCL;
    }
    public String getPind1() {
        return pinD1;
    }

    public void setPind1(String pinD1) {
        this.pinD1 = pinD1;
    }
    public String getPina0() {
        return pinA0;
    }

    public void setPina0(String pinA0) {
        this.pinA0 = pinA0;
    }
    public String getPind3() {
        return pinD3;
    }

    public void setPind3(String pinD3) {
        this.pinD3 = pinD3;
    }
    public String getPind5() {
        return pinD5;
    }

    public void setPind5(String pinD5) {
        this.pinD5 = pinD5;
    }


}