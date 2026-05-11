





import java.util.List;
import java.util.ArrayList;

public class cloudml_DeploymentModel extends WithProperties {






    private List<cloudml_Provider> cloudml_providers;




    private List<cloudml_Binding> cloudml_bindings;




    private List<cloudml_NodeInstance> cloudml_nodeinstances;




    private List<cloudml_ArtefactInstance> cloudml_artefactinstances;




    private List<cloudml_Node> cloudml_nodes;




    private List<cloudml_BindingInstance> cloudml_bindinginstances;


    public cloudml_DeploymentModel(
    ) {
        super(
        );
        this.cloudml_providers = new ArrayList<>();
        this.cloudml_bindings = new ArrayList<>();
        this.cloudml_nodeinstances = new ArrayList<>();
        this.cloudml_artefactinstances = new ArrayList<>();
        this.cloudml_nodes = new ArrayList<>();
        this.cloudml_bindinginstances = new ArrayList<>();
    }

    public cloudml_DeploymentModel(
        ArrayList<cloudml_Provider> cloudml_providers,        ArrayList<cloudml_Binding> cloudml_bindings,        ArrayList<cloudml_NodeInstance> cloudml_nodeinstances,        ArrayList<cloudml_ArtefactInstance> cloudml_artefactinstances,        ArrayList<cloudml_Node> cloudml_nodes,        ArrayList<cloudml_BindingInstance> cloudml_bindinginstances    ) {
        this.cloudml_providers = cloudml_providers;
        this.cloudml_bindings = cloudml_bindings;
        this.cloudml_nodeinstances = cloudml_nodeinstances;
        this.cloudml_artefactinstances = cloudml_artefactinstances;
        this.cloudml_nodes = cloudml_nodes;
        this.cloudml_bindinginstances = cloudml_bindinginstances;
    }


    public List<cloudml_Provider> getCloudml_providers() {
        return cloudml_providers;
    }

    public void addCloudml_provider(Cloudml_provider cloudml_provider) {
        this.cloudml_providers.add(cloudml_provider);
    }
    public List<cloudml_Binding> getCloudml_bindings() {
        return cloudml_bindings;
    }

    public void addCloudml_binding(Cloudml_binding cloudml_binding) {
        this.cloudml_bindings.add(cloudml_binding);
    }
    public List<cloudml_NodeInstance> getCloudml_nodeinstances() {
        return cloudml_nodeinstances;
    }

    public void addCloudml_nodeinstance(Cloudml_nodeinstance cloudml_nodeinstance) {
        this.cloudml_nodeinstances.add(cloudml_nodeinstance);
    }
    public List<cloudml_ArtefactInstance> getCloudml_artefactinstances() {
        return cloudml_artefactinstances;
    }

    public void addCloudml_artefactinstance(Cloudml_artefactinstance cloudml_artefactinstance) {
        this.cloudml_artefactinstances.add(cloudml_artefactinstance);
    }
    public List<cloudml_Node> getCloudml_nodes() {
        return cloudml_nodes;
    }

    public void addCloudml_node(Cloudml_node cloudml_node) {
        this.cloudml_nodes.add(cloudml_node);
    }
    public List<cloudml_BindingInstance> getCloudml_bindinginstances() {
        return cloudml_bindinginstances;
    }

    public void addCloudml_bindinginstance(Cloudml_bindinginstance cloudml_bindinginstance) {
        this.cloudml_bindinginstances.add(cloudml_bindinginstance);
    }

}