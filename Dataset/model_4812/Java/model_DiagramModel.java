





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModel extends ZentaModelElement, Documentable, Properties, DiagramModelContainer {

    private int connectionRouterType;





    private model_DiagramModelComponent model_diagrammodelcomponent;


    public model_DiagramModel(
        int connectionRouterType    ) {
        super(
        );
        this.connectionRouterType = connectionRouterType;
    }


    public int getConnectionroutertype() {
        return connectionRouterType;
    }

    public void setConnectionroutertype(int connectionRouterType) {
        this.connectionRouterType = connectionRouterType;
    }

    public model_DiagramModelComponent getModel_diagrammodelcomponent() {
        return model_diagrammodelcomponent;
    }

    public void setModel_diagrammodelcomponent(model_DiagramModelComponent model_diagrammodelcomponent) {
        this.model_diagrammodelcomponent = model_diagrammodelcomponent;
    }

}