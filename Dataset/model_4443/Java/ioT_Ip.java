





import java.util.List;
import java.util.ArrayList;

public class ioT_Ip  {

    private int ip;





    private ioT_Server iot_server;


    public ioT_Ip(
        int ip    ) {
        this.ip = ip;
    }


    public int getIp() {
        return ip;
    }

    public void setIp(int ip) {
        this.ip = ip;
    }

    public ioT_Server getIot_server() {
        return iot_server;
    }

    public void setIot_server(ioT_Server iot_server) {
        this.iot_server = iot_server;
    }

}