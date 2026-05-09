





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_Event extends Element {

    private String model;
    private String type;





    private List<MMInterModel_Transition> mmintermodel_transitions;




    private MMInterModel_Model mmintermodel_model;




    private MMInterModel_Transition mmintermodel_transition;


    public MMInterModel_Event(
        String model,        String type    ) {
        super(
        );
        this.model = model;
        this.type = type;
        this.mmintermodel_transitions = new ArrayList<>();
    }

    public MMInterModel_Event(
        String model,        String type        ArrayList<MMInterModel_Transition> mmintermodel_transitions    ) {
        this.model = model;
        this.type = type;
        this.mmintermodel_transitions = mmintermodel_transitions;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<MMInterModel_Transition> getMmintermodel_transitions() {
        return mmintermodel_transitions;
    }

    public void addMmintermodel_transition(Mmintermodel_transition mmintermodel_transition) {
        this.mmintermodel_transitions.add(mmintermodel_transition);
    }
    public MMInterModel_Model getMmintermodel_model() {
        return mmintermodel_model;
    }

    public void setMmintermodel_model(MMInterModel_Model mmintermodel_model) {
        this.mmintermodel_model = mmintermodel_model;
    }
    public MMInterModel_Transition getMmintermodel_transition() {
        return mmintermodel_transition;
    }

    public void setMmintermodel_transition(MMInterModel_Transition mmintermodel_transition) {
        this.mmintermodel_transition = mmintermodel_transition;
    }

}