





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_Component extends Element {

    private String model;
    private int numberOfSpares;





    private List<MMInterModel_Attribute> mmintermodel_attributes;




    private List<MMInterModel_StateMachine> mmintermodel_statemachines;




    private MMInterModel_StateMachine mmintermodel_statemachine;




    private MMInterModel_Model mmintermodel_model;


    public MMInterModel_Component(
        String model,        int numberOfSpares    ) {
        super(
        );
        this.model = model;
        this.numberOfSpares = numberOfSpares;
        this.mmintermodel_attributes = new ArrayList<>();
        this.mmintermodel_statemachines = new ArrayList<>();
    }

    public MMInterModel_Component(
        String model,        int numberOfSpares        ArrayList<MMInterModel_Attribute> mmintermodel_attributes,        ArrayList<MMInterModel_StateMachine> mmintermodel_statemachines    ) {
        this.model = model;
        this.numberOfSpares = numberOfSpares;
        this.mmintermodel_attributes = mmintermodel_attributes;
        this.mmintermodel_statemachines = mmintermodel_statemachines;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public int getNumberofspares() {
        return numberOfSpares;
    }

    public void setNumberofspares(int numberOfSpares) {
        this.numberOfSpares = numberOfSpares;
    }

    public List<MMInterModel_Attribute> getMmintermodel_attributes() {
        return mmintermodel_attributes;
    }

    public void addMmintermodel_attribute(Mmintermodel_attribute mmintermodel_attribute) {
        this.mmintermodel_attributes.add(mmintermodel_attribute);
    }
    public List<MMInterModel_StateMachine> getMmintermodel_statemachines() {
        return mmintermodel_statemachines;
    }

    public void addMmintermodel_statemachine(Mmintermodel_statemachine mmintermodel_statemachine) {
        this.mmintermodel_statemachines.add(mmintermodel_statemachine);
    }
    public MMInterModel_StateMachine getMmintermodel_statemachine() {
        return mmintermodel_statemachine;
    }

    public void setMmintermodel_statemachine(MMInterModel_StateMachine mmintermodel_statemachine) {
        this.mmintermodel_statemachine = mmintermodel_statemachine;
    }
    public MMInterModel_Model getMmintermodel_model() {
        return mmintermodel_model;
    }

    public void setMmintermodel_model(MMInterModel_Model mmintermodel_model) {
        this.mmintermodel_model = mmintermodel_model;
    }

}