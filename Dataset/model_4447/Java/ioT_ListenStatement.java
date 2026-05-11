





import java.util.List;
import java.util.ArrayList;

public class ioT_ListenStatement  {

    private String ip;
    private int port;





    private ioT_Program iot_program;


    public ioT_ListenStatement(
        String ip,        int port    ) {
        this.ip = ip;
        this.port = port;
    }


    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public ioT_Program getIot_program() {
        return iot_program;
    }

    public void setIot_program(ioT_Program iot_program) {
        this.iot_program = iot_program;
    }

}