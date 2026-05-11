





import java.util.List;
import java.util.ArrayList;

public class model_BasicRelationship extends BasicObject {






    private model_ZentaElement model_zentaelement;




    private model_ZentaElement model_zentaelement;




    private model_DiagramModelZentaConnection model_diagrammodelzentaconnection;




    private List<model_DiagramModelZentaConnection> model_diagrammodelzentaconnections;


    public model_BasicRelationship(
    ) {
        super(
        );
        this.model_diagrammodelzentaconnections = new ArrayList<>();
    }

    public model_BasicRelationship(
        ArrayList<model_DiagramModelZentaConnection> model_diagrammodelzentaconnections    ) {
        this.model_diagrammodelzentaconnections = model_diagrammodelzentaconnections;
    }


    public model_ZentaElement getModel_zentaelement() {
        return model_zentaelement;
    }

    public void setModel_zentaelement(model_ZentaElement model_zentaelement) {
        this.model_zentaelement = model_zentaelement;
    }
    public model_ZentaElement getModel_zentaelement() {
        return model_zentaelement;
    }

    public void setModel_zentaelement(model_ZentaElement model_zentaelement) {
        this.model_zentaelement = model_zentaelement;
    }
    public model_DiagramModelZentaConnection getModel_diagrammodelzentaconnection() {
        return model_diagrammodelzentaconnection;
    }

    public void setModel_diagrammodelzentaconnection(model_DiagramModelZentaConnection model_diagrammodelzentaconnection) {
        this.model_diagrammodelzentaconnection = model_diagrammodelzentaconnection;
    }
    public List<model_DiagramModelZentaConnection> getModel_diagrammodelzentaconnections() {
        return model_diagrammodelzentaconnections;
    }

    public void addModel_diagrammodelzentaconnection(Model_diagrammodelzentaconnection model_diagrammodelzentaconnection) {
        this.model_diagrammodelzentaconnections.add(model_diagrammodelzentaconnection);
    }

}