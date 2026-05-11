





import java.util.List;
import java.util.ArrayList;

public class goatInfrastructure_SingleServer extends Infrastructure {

    private int timeout;
    private String server;



    public goatInfrastructure_SingleServer(
        int timeout,        String server    ) {
        super(
        );
        this.timeout = timeout;
        this.server = server;
    }


    public int getTimeout() {
        return timeout;
    }

    public void setTimeout(int timeout) {
        this.timeout = timeout;
    }
    public String getServer() {
        return server;
    }

    public void setServer(String server) {
        this.server = server;
    }


}