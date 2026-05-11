





import java.util.List;
import java.util.ArrayList;

public class cloudml_CloudMLModel extends CloudMLElementWithProperties {






    private List<cloudml_Cloud> cloudml_clouds;




    private List<cloudml_ComponentInstance> cloudml_componentinstances;




    private List<cloudml_Component> cloudml_components;




    private List<cloudml_Provider> cloudml_providers;




    private List<cloudml_ExecuteInstance> cloudml_executeinstances;




    private List<cloudml_Relationship> cloudml_relationships;


    public cloudml_CloudMLModel(
    ) {
        super(
        );
        this.cloudml_clouds = new ArrayList<>();
        this.cloudml_componentinstances = new ArrayList<>();
        this.cloudml_components = new ArrayList<>();
        this.cloudml_providers = new ArrayList<>();
        this.cloudml_executeinstances = new ArrayList<>();
        this.cloudml_relationships = new ArrayList<>();
    }

    public cloudml_CloudMLModel(
        ArrayList<cloudml_Cloud> cloudml_clouds,        ArrayList<cloudml_ComponentInstance> cloudml_componentinstances,        ArrayList<cloudml_Component> cloudml_components,        ArrayList<cloudml_Provider> cloudml_providers,        ArrayList<cloudml_ExecuteInstance> cloudml_executeinstances,        ArrayList<cloudml_Relationship> cloudml_relationships    ) {
        this.cloudml_clouds = cloudml_clouds;
        this.cloudml_componentinstances = cloudml_componentinstances;
        this.cloudml_components = cloudml_components;
        this.cloudml_providers = cloudml_providers;
        this.cloudml_executeinstances = cloudml_executeinstances;
        this.cloudml_relationships = cloudml_relationships;
    }


    public List<cloudml_Cloud> getCloudml_clouds() {
        return cloudml_clouds;
    }

    public void addCloudml_cloud(Cloudml_cloud cloudml_cloud) {
        this.cloudml_clouds.add(cloudml_cloud);
    }
    public List<cloudml_ComponentInstance> getCloudml_componentinstances() {
        return cloudml_componentinstances;
    }

    public void addCloudml_componentinstance(Cloudml_componentinstance cloudml_componentinstance) {
        this.cloudml_componentinstances.add(cloudml_componentinstance);
    }
    public List<cloudml_Component> getCloudml_components() {
        return cloudml_components;
    }

    public void addCloudml_component(Cloudml_component cloudml_component) {
        this.cloudml_components.add(cloudml_component);
    }
    public List<cloudml_Provider> getCloudml_providers() {
        return cloudml_providers;
    }

    public void addCloudml_provider(Cloudml_provider cloudml_provider) {
        this.cloudml_providers.add(cloudml_provider);
    }
    public List<cloudml_ExecuteInstance> getCloudml_executeinstances() {
        return cloudml_executeinstances;
    }

    public void addCloudml_executeinstance(Cloudml_executeinstance cloudml_executeinstance) {
        this.cloudml_executeinstances.add(cloudml_executeinstance);
    }
    public List<cloudml_Relationship> getCloudml_relationships() {
        return cloudml_relationships;
    }

    public void addCloudml_relationship(Cloudml_relationship cloudml_relationship) {
        this.cloudml_relationships.add(cloudml_relationship);
    }

}