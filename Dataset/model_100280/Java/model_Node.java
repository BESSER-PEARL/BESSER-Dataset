





import java.util.List;
import java.util.ArrayList;

public class model_Node extends Object {






    private List<model_Arc> model_arcs;




    private List<model_Arc> model_arcs;




    private model_Arc model_arc;




    private model_Arc model_arc;


    public model_Node(
    ) {
        super(
        );
        this.model_arcs = new ArrayList<>();
        this.model_arcs = new ArrayList<>();
    }

    public model_Node(
        ArrayList<model_Arc> model_arcs,        ArrayList<model_Arc> model_arcs    ) {
        this.model_arcs = model_arcs;
        this.model_arcs = model_arcs;
    }


    public List<model_Arc> getModel_arcs() {
        return model_arcs;
    }

    public void addModel_arc(Model_arc model_arc) {
        this.model_arcs.add(model_arc);
    }
    public List<model_Arc> getModel_arcs() {
        return model_arcs;
    }

    public void addModel_arc(Model_arc model_arc) {
        this.model_arcs.add(model_arc);
    }
    public model_Arc getModel_arc() {
        return model_arc;
    }

    public void setModel_arc(model_Arc model_arc) {
        this.model_arc = model_arc;
    }
    public model_Arc getModel_arc() {
        return model_arc;
    }

    public void setModel_arc(model_Arc model_arc) {
        this.model_arc = model_arc;
    }

}