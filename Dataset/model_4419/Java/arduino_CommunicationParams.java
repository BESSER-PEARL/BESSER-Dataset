





import java.util.List;
import java.util.ArrayList;

public class arduino_CommunicationParams  {

    private String mac;
    private String subnet;
    private int baudrate;
    private String dns;
    private String gateway;
    private String ip;
    private String type;





    private arduino_SystemDefinition arduino_systemdefinition;


    public arduino_CommunicationParams(
        String mac,        String subnet,        int baudrate,        String dns,        String gateway,        String ip,        String type    ) {
        this.mac = mac;
        this.subnet = subnet;
        this.baudrate = baudrate;
        this.dns = dns;
        this.gateway = gateway;
        this.ip = ip;
        this.type = type;
    }


    public String getMac() {
        return mac;
    }

    public void setMac(String mac) {
        this.mac = mac;
    }
    public String getSubnet() {
        return subnet;
    }

    public void setSubnet(String subnet) {
        this.subnet = subnet;
    }
    public int getBaudrate() {
        return baudrate;
    }

    public void setBaudrate(int baudrate) {
        this.baudrate = baudrate;
    }
    public String getDns() {
        return dns;
    }

    public void setDns(String dns) {
        this.dns = dns;
    }
    public String getGateway() {
        return gateway;
    }

    public void setGateway(String gateway) {
        this.gateway = gateway;
    }
    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public arduino_SystemDefinition getArduino_systemdefinition() {
        return arduino_systemdefinition;
    }

    public void setArduino_systemdefinition(arduino_SystemDefinition arduino_systemdefinition) {
        this.arduino_systemdefinition = arduino_systemdefinition;
    }

}