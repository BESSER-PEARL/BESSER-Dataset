





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_MessageBroker  {

    private String usser;
    private String type;
    private String pass_;
    private int port;
    private String host;



    public wsmodel3_MessageBroker(
        String usser,        String type,        String pass_,        int port,        String host    ) {
        this.usser = usser;
        this.type = type;
        this.pass_ = pass_;
        this.port = port;
        this.host = host;
    }


    public String getUsser() {
        return usser;
    }

    public void setUsser(String usser) {
        this.usser = usser;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPass_() {
        return pass_;
    }

    public void setPass_(String pass_) {
        this.pass_ = pass_;
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