





import java.util.List;
import java.util.ArrayList;

public class model_Page extends HasLabel, HasName, HasId {






    private model_Object model_object;




    private model_PetriNet model_petrinet;




    private List<model_Object> model_objects;




    private model_Arc model_arc;




    private model_PetriNet model_petrinet;




    private List<model_Arc> model_arcs;


    public model_Page(
    ) {
        super(
        );
        this.model_objects = new ArrayList<>();
        this.model_arcs = new ArrayList<>();
    }

    public model_Page(
        ArrayList<model_Object> model_objects,        ArrayList<model_Arc> model_arcs    ) {
        this.model_objects = model_objects;
        this.model_arcs = model_arcs;
    }


    public model_Object getModel_object() {
        return model_object;
    }

    public void setModel_object(model_Object model_object) {
        this.model_object = model_object;
    }
    public model_PetriNet getModel_petrinet() {
        return model_petrinet;
    }

    public void setModel_petrinet(model_PetriNet model_petrinet) {
        this.model_petrinet = model_petrinet;
    }
    public List<model_Object> getModel_objects() {
        return model_objects;
    }

    public void addModel_object(Model_object model_object) {
        this.model_objects.add(model_object);
    }
    public model_Arc getModel_arc() {
        return model_arc;
    }

    public void setModel_arc(model_Arc model_arc) {
        this.model_arc = model_arc;
    }
    public model_PetriNet getModel_petrinet() {
        return model_petrinet;
    }

    public void setModel_petrinet(model_PetriNet model_petrinet) {
        this.model_petrinet = model_petrinet;
    }
    public List<model_Arc> getModel_arcs() {
        return model_arcs;
    }

    public void addModel_arc(Model_arc model_arc) {
        this.model_arcs.add(model_arc);
    }

}