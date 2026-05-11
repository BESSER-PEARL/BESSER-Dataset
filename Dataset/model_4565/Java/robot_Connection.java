





import java.util.List;
import java.util.ArrayList;

public class robot_Connection  {

    private int port;
    private String ip;



    public robot_Connection(
        int port,        String ip    ) {
        this.port = port;
        this.ip = ip;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }


}