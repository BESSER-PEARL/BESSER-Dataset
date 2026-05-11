





import java.util.List;
import java.util.ArrayList;

public class cloudml_RequiredExecutionPlatform extends ExecutionPlatform {






    private List<cloudml_Property> cloudml_propertys;




    private cloudml_InternalComponent cloudml_internalcomponent;


    public cloudml_RequiredExecutionPlatform(
    ) {
        super(
        );
        this.cloudml_propertys = new ArrayList<>();
    }

    public cloudml_RequiredExecutionPlatform(
        ArrayList<cloudml_Property> cloudml_propertys    ) {
        this.cloudml_propertys = cloudml_propertys;
    }


    public List<cloudml_Property> getCloudml_propertys() {
        return cloudml_propertys;
    }

    public void addCloudml_property(Cloudml_property cloudml_property) {
        this.cloudml_propertys.add(cloudml_property);
    }
    public cloudml_InternalComponent getCloudml_internalcomponent() {
        return cloudml_internalcomponent;
    }

    public void setCloudml_internalcomponent(cloudml_InternalComponent cloudml_internalcomponent) {
        this.cloudml_internalcomponent = cloudml_internalcomponent;
    }

}