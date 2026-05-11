





import java.util.List;
import java.util.ArrayList;

public class model_Connectable extends DiagramModelComponent {






    private model_DiagramModelConnection model_diagrammodelconnection;




    private List<model_DiagramModelConnection> model_diagrammodelconnections;




    private model_DiagramModelConnection model_diagrammodelconnection;




    private List<model_DiagramModelConnection> model_diagrammodelconnections;


    public model_Connectable(
    ) {
        super(
        );
        this.model_diagrammodelconnections = new ArrayList<>();
        this.model_diagrammodelconnections = new ArrayList<>();
    }

    public model_Connectable(
        ArrayList<model_DiagramModelConnection> model_diagrammodelconnections,        ArrayList<model_DiagramModelConnection> model_diagrammodelconnections    ) {
        this.model_diagrammodelconnections = model_diagrammodelconnections;
        this.model_diagrammodelconnections = model_diagrammodelconnections;
    }


    public model_DiagramModelConnection getModel_diagrammodelconnection() {
        return model_diagrammodelconnection;
    }

    public void setModel_diagrammodelconnection(model_DiagramModelConnection model_diagrammodelconnection) {
        this.model_diagrammodelconnection = model_diagrammodelconnection;
    }
    public List<model_DiagramModelConnection> getModel_diagrammodelconnections() {
        return model_diagrammodelconnections;
    }

    public void addModel_diagrammodelconnection(Model_diagrammodelconnection model_diagrammodelconnection) {
        this.model_diagrammodelconnections.add(model_diagrammodelconnection);
    }
    public model_DiagramModelConnection getModel_diagrammodelconnection() {
        return model_diagrammodelconnection;
    }

    public void setModel_diagrammodelconnection(model_DiagramModelConnection model_diagrammodelconnection) {
        this.model_diagrammodelconnection = model_diagrammodelconnection;
    }
    public List<model_DiagramModelConnection> getModel_diagrammodelconnections() {
        return model_diagrammodelconnections;
    }

    public void addModel_diagrammodelconnection(Model_diagrammodelconnection model_diagrammodelconnection) {
        this.model_diagrammodelconnections.add(model_diagrammodelconnection);
    }

}