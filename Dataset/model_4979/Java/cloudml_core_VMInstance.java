





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VMInstance extends ExternalComponentInstance {

    private String publicAddress;
    private String id;



    public cloudml_core_VMInstance(
        String publicAddress,        String id    ) {
        super(
        );
        this.publicAddress = publicAddress;
        this.id = id;
    }


    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}