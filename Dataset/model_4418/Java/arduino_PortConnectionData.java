





import java.util.List;
import java.util.ArrayList;

public class arduino_PortConnectionData  {

    private String host;
    private int port;





    private arduino_PortTCP arduino_porttcp;


    public arduino_PortConnectionData(
        String host,        int port    ) {
        this.host = host;
        this.port = port;
    }


    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public arduino_PortTCP getArduino_porttcp() {
        return arduino_porttcp;
    }

    public void setArduino_porttcp(arduino_PortTCP arduino_porttcp) {
        this.arduino_porttcp = arduino_porttcp;
    }

}