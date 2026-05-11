





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_NodeInstance extends WithProperties {

    private String publicAddress;





    private NodeInstance nodeinstance;


    public cloudml_core_NodeInstance(
        String publicAddress    ) {
        super(
        );
        this.publicAddress = publicAddress;
    }


    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }

    public NodeInstance getNodeinstance() {
        return nodeinstance;
    }

    public void setNodeinstance(NodeInstance nodeinstance) {
        this.nodeinstance = nodeinstance;
    }

}