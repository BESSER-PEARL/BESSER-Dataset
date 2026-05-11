





import java.util.List;
import java.util.ArrayList;

public class cloudml_ProvidedExecutionPlatform extends ExecutionPlatform {






    private List<cloudml_Property> cloudml_propertys;




    private cloudml_Component cloudml_component;


    public cloudml_ProvidedExecutionPlatform(
    ) {
        super(
        );
        this.cloudml_propertys = new ArrayList<>();
    }

    public cloudml_ProvidedExecutionPlatform(
        ArrayList<cloudml_Property> cloudml_propertys    ) {
        this.cloudml_propertys = cloudml_propertys;
    }


    public List<cloudml_Property> getCloudml_propertys() {
        return cloudml_propertys;
    }

    public void addCloudml_property(Cloudml_property cloudml_property) {
        this.cloudml_propertys.add(cloudml_property);
    }
    public cloudml_Component getCloudml_component() {
        return cloudml_component;
    }

    public void setCloudml_component(cloudml_Component cloudml_component) {
        this.cloudml_component = cloudml_component;
    }

}