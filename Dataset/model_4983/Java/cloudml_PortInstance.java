





import java.util.List;
import java.util.ArrayList;

public class cloudml_PortInstance extends CloudMLElementWithProperties {






    private cloudml_ComponentInstance cloudml_componentinstance;




    private cloudml_Port cloudml_port;


    public cloudml_PortInstance(
    ) {
        super(
        );
    }



    public cloudml_ComponentInstance getCloudml_componentinstance() {
        return cloudml_componentinstance;
    }

    public void setCloudml_componentinstance(cloudml_ComponentInstance cloudml_componentinstance) {
        this.cloudml_componentinstance = cloudml_componentinstance;
    }
    public cloudml_Port getCloudml_port() {
        return cloudml_port;
    }

    public void setCloudml_port(cloudml_Port cloudml_port) {
        this.cloudml_port = cloudml_port;
    }

}