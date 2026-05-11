





import java.util.List;
import java.util.ArrayList;

public class arduino_ExplicitSupportData extends SupportData {

    private int port;
    private String host;



    public arduino_ExplicitSupportData(
        int port,        String host    ) {
        super(
        );
        this.port = port;
        this.host = host;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }


}