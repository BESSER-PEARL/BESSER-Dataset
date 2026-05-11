





import java.util.List;
import java.util.ArrayList;

public class cloudml_NodeInstance extends WithProperties {

    private String publicAddress;
    private String id;





    private cloudml_Node cloudml_node;


    public cloudml_NodeInstance(
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

    public cloudml_Node getCloudml_node() {
        return cloudml_node;
    }

    public void setCloudml_node(cloudml_Node cloudml_node) {
        this.cloudml_node = cloudml_node;
    }

}