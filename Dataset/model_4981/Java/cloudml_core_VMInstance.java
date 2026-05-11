





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VMInstance extends ExternalComponentInstance {

    private String id;
    private String publicAddress;



    public cloudml_core_VMInstance(
        String id,        String publicAddress    ) {
        super(
        );
        this.id = id;
        this.publicAddress = publicAddress;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }


}