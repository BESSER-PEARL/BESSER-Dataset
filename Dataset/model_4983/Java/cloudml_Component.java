





import java.util.List;
import java.util.ArrayList;

public class cloudml_Component extends CloudMLElementWithProperties {






    private cloudml_ExecutionPlatform cloudml_executionplatform;




    private cloudml_Port cloudml_port;




    private cloudml_ComponentInstance cloudml_componentinstance;


    public cloudml_Component(
    ) {
        super(
        );
    }



    public cloudml_ExecutionPlatform getCloudml_executionplatform() {
        return cloudml_executionplatform;
    }

    public void setCloudml_executionplatform(cloudml_ExecutionPlatform cloudml_executionplatform) {
        this.cloudml_executionplatform = cloudml_executionplatform;
    }
    public cloudml_Port getCloudml_port() {
        return cloudml_port;
    }

    public void setCloudml_port(cloudml_Port cloudml_port) {
        this.cloudml_port = cloudml_port;
    }
    public cloudml_ComponentInstance getCloudml_componentinstance() {
        return cloudml_componentinstance;
    }

    public void setCloudml_componentinstance(cloudml_ComponentInstance cloudml_componentinstance) {
        this.cloudml_componentinstance = cloudml_componentinstance;
    }

}