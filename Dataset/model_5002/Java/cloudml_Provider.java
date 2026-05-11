





import java.util.List;
import java.util.ArrayList;

public class cloudml_Provider extends WithProperties {

    private String credentials;





    private cloudml_Node cloudml_node;


    public cloudml_Provider(
        String credentials    ) {
        super(
        );
        this.credentials = credentials;
    }


    public String getCredentials() {
        return credentials;
    }

    public void setCredentials(String credentials) {
        this.credentials = credentials;
    }

    public cloudml_Node getCloudml_node() {
        return cloudml_node;
    }

    public void setCloudml_node(cloudml_Node cloudml_node) {
        this.cloudml_node = cloudml_node;
    }

}