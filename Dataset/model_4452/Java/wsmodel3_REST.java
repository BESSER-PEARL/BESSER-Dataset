





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_REST  {

    private String URI;
    private int port;





    private wsmodel3_Device wsmodel3_device;


    public wsmodel3_REST(
        String URI,        int port    ) {
        this.URI = URI;
        this.port = port;
    }


    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public wsmodel3_Device getWsmodel3_device() {
        return wsmodel3_device;
    }

    public void setWsmodel3_device(wsmodel3_Device wsmodel3_device) {
        this.wsmodel3_device = wsmodel3_device;
    }

}