





import java.util.List;
import java.util.ArrayList;

public class arduino_CommunicationParams  {

    private String ip;
    private String type;
    private String gateway;
    private String dns;
    private String subnet;
    private int baudrate;
    private String mac;





    private arduino_SystemDefinition arduino_systemdefinition;


    public arduino_CommunicationParams(
        String ip,        String type,        String gateway,        String dns,        String subnet,        int baudrate,        String mac    ) {
        this.ip = ip;
        this.type = type;
        this.gateway = gateway;
        this.dns = dns;
        this.subnet = subnet;
        this.baudrate = baudrate;
        this.mac = mac;
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
    public String getMac() {
        return mac;
    }

    public void setMac(String mac) {
        this.mac = mac;
    }

    public arduino_SystemDefinition getArduino_systemdefinition() {
        return arduino_systemdefinition;
    }

    public void setArduino_systemdefinition(arduino_SystemDefinition arduino_systemdefinition) {
        this.arduino_systemdefinition = arduino_systemdefinition;
    }

}