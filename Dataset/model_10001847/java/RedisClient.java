





import java.util.List;
import java.util.ArrayList;

public class RedisClient  {

    private String log;
    private String RadixClient;
    private String email;



    public RedisClient(
        String log,        String RadixClient,        String email    ) {
        this.log = log;
        this.RadixClient = RadixClient;
        this.email = email;
    }


    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
    }
    public String getRadixclient() {
        return RadixClient;
    }

    public void setRadixclient(String RadixClient) {
        this.RadixClient = RadixClient;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}