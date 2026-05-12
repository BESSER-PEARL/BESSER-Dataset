





import java.util.List;
import java.util.ArrayList;

public class PremiumCustomer  {

    private String email;
    private String log;
    private String RadixClient;



    public PremiumCustomer(
        String email,        String log,        String RadixClient    ) {
        this.email = email;
        this.log = log;
        this.RadixClient = RadixClient;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
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


}