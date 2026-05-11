





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VMInstance extends ExternalComponentInstance {

    private String publicAddress;
    private String hostname;
    private String id;



    public cloudml_core_VMInstance(
        String publicAddress,        String hostname,        String id    ) {
        super(
        );
        this.publicAddress = publicAddress;
        this.hostname = hostname;
        this.id = id;
    }


    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }
    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}