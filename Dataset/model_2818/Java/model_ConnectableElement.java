





import java.util.List;
import java.util.ArrayList;

public class model_ConnectableElement extends FeatureContainer {






    private model_Node model_node;




    private List<model_FeatureContainer> model_featurecontainers;


    public model_ConnectableElement(
    ) {
        super(
        );
        this.model_featurecontainers = new ArrayList<>();
    }

    public model_ConnectableElement(
        ArrayList<model_FeatureContainer> model_featurecontainers    ) {
        this.model_featurecontainers = model_featurecontainers;
    }


    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }
    public List<model_FeatureContainer> getModel_featurecontainers() {
        return model_featurecontainers;
    }

    public void addModel_featurecontainer(Model_featurecontainer model_featurecontainer) {
        this.model_featurecontainers.add(model_featurecontainer);
    }

}