





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelObject extends FontAttribute, DiagramModelComponent {

    private String fillColor;





    private List<model_DiagramModelConnection> model_diagrammodelconnections;




    private List<model_DiagramModelConnection> model_diagrammodelconnections;




    private model_DiagramModelContainer model_diagrammodelcontainer;




    private model_DiagramModelConnection model_diagrammodelconnection;




    private model_DiagramModelConnection model_diagrammodelconnection;


    public model_DiagramModelObject(
        String fillColor    ) {
        super(
        );
        this.fillColor = fillColor;
        this.model_diagrammodelconnections = new ArrayList<>();
        this.model_diagrammodelconnections = new ArrayList<>();
    }

    public model_DiagramModelObject(
        String fillColor        ArrayList<model_DiagramModelConnection> model_diagrammodelconnections,        ArrayList<model_DiagramModelConnection> model_diagrammodelconnections    ) {
        this.fillColor = fillColor;
        this.model_diagrammodelconnections = model_diagrammodelconnections;
        this.model_diagrammodelconnections = model_diagrammodelconnections;
    }

    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }

    public List<model_DiagramModelConnection> getModel_diagrammodelconnections() {
        return model_diagrammodelconnections;
    }

    public void addModel_diagrammodelconnection(Model_diagrammodelconnection model_diagrammodelconnection) {
        this.model_diagrammodelconnections.add(model_diagrammodelconnection);
    }
    public List<model_DiagramModelConnection> getModel_diagrammodelconnections() {
        return model_diagrammodelconnections;
    }

    public void addModel_diagrammodelconnection(Model_diagrammodelconnection model_diagrammodelconnection) {
        this.model_diagrammodelconnections.add(model_diagrammodelconnection);
    }
    public model_DiagramModelContainer getModel_diagrammodelcontainer() {
        return model_diagrammodelcontainer;
    }

    public void setModel_diagrammodelcontainer(model_DiagramModelContainer model_diagrammodelcontainer) {
        this.model_diagrammodelcontainer = model_diagrammodelcontainer;
    }
    public model_DiagramModelConnection getModel_diagrammodelconnection() {
        return model_diagrammodelconnection;
    }

    public void setModel_diagrammodelconnection(model_DiagramModelConnection model_diagrammodelconnection) {
        this.model_diagrammodelconnection = model_diagrammodelconnection;
    }
    public model_DiagramModelConnection getModel_diagrammodelconnection() {
        return model_diagrammodelconnection;
    }

    public void setModel_diagrammodelconnection(model_DiagramModelConnection model_diagrammodelconnection) {
        this.model_diagrammodelconnection = model_diagrammodelconnection;
    }

}