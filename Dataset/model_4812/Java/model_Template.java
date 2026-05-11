





import java.util.List;
import java.util.ArrayList;

public class model_Template  {

    private String path;





    private List<model_BasicObject> model_basicobjects;




    private model_Metamodel model_metamodel;




    private model_DiagramModel model_diagrammodel;




    private model_Metamodel model_metamodel;




    private model_BasicObject model_basicobject;


    public model_Template(
        String path    ) {
        this.path = path;
        this.model_basicobjects = new ArrayList<>();
    }

    public model_Template(
        String path        ArrayList<model_BasicObject> model_basicobjects    ) {
        this.path = path;
        this.model_basicobjects = model_basicobjects;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public List<model_BasicObject> getModel_basicobjects() {
        return model_basicobjects;
    }

    public void addModel_basicobject(Model_basicobject model_basicobject) {
        this.model_basicobjects.add(model_basicobject);
    }
    public model_Metamodel getModel_metamodel() {
        return model_metamodel;
    }

    public void setModel_metamodel(model_Metamodel model_metamodel) {
        this.model_metamodel = model_metamodel;
    }
    public model_DiagramModel getModel_diagrammodel() {
        return model_diagrammodel;
    }

    public void setModel_diagrammodel(model_DiagramModel model_diagrammodel) {
        this.model_diagrammodel = model_diagrammodel;
    }
    public model_Metamodel getModel_metamodel() {
        return model_metamodel;
    }

    public void setModel_metamodel(model_Metamodel model_metamodel) {
        this.model_metamodel = model_metamodel;
    }
    public model_BasicObject getModel_basicobject() {
        return model_basicobject;
    }

    public void setModel_basicobject(model_BasicObject model_basicobject) {
        this.model_basicobject = model_basicobject;
    }

}