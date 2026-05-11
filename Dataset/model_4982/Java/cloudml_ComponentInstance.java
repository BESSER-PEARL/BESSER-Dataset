





import java.util.List;
import java.util.ArrayList;

public class cloudml_ComponentInstance extends CloudMLElementWithProperties {






    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private cloudml_ExecutionPlatformInstance cloudml_executionplatforminstance;




    private cloudml_PortInstance cloudml_portinstance;




    private cloudml_Component cloudml_component;


    public cloudml_ComponentInstance(
    ) {
        super(
        );
    }



    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }
    public cloudml_ExecutionPlatformInstance getCloudml_executionplatforminstance() {
        return cloudml_executionplatforminstance;
    }

    public void setCloudml_executionplatforminstance(cloudml_ExecutionPlatformInstance cloudml_executionplatforminstance) {
        this.cloudml_executionplatforminstance = cloudml_executionplatforminstance;
    }
    public cloudml_PortInstance getCloudml_portinstance() {
        return cloudml_portinstance;
    }

    public void setCloudml_portinstance(cloudml_PortInstance cloudml_portinstance) {
        this.cloudml_portinstance = cloudml_portinstance;
    }
    public cloudml_Component getCloudml_component() {
        return cloudml_component;
    }

    public void setCloudml_component(cloudml_Component cloudml_component) {
        this.cloudml_component = cloudml_component;
    }

}