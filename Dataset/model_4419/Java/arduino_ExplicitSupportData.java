





import java.util.List;
import java.util.ArrayList;

public class arduino_ExplicitSupportData extends SupportData {

    private String host;
    private int port;



    public arduino_ExplicitSupportData(
        String host,        int port    ) {
        super(
        );
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


}