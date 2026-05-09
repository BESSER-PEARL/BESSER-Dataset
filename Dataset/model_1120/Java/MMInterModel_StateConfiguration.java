





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_StateConfiguration extends Element {

    private String configOperator;
    private String condition;
    private String model;
    private boolean negation;





    private MMInterModel_StateConfiguration mmintermodel_stateconfiguration;




    private List<MMInterModel_State> mmintermodel_states;




    private MMInterModel_Model mmintermodel_model;


    public MMInterModel_StateConfiguration(
        String configOperator,        String condition,        String model,        boolean negation    ) {
        super(
        );
        this.configOperator = configOperator;
        this.condition = condition;
        this.model = model;
        this.negation = negation;
        this.mmintermodel_states = new ArrayList<>();
    }

    public MMInterModel_StateConfiguration(
        String configOperator,        String condition,        String model,        boolean negation        ArrayList<MMInterModel_State> mmintermodel_states    ) {
        this.configOperator = configOperator;
        this.condition = condition;
        this.model = model;
        this.negation = negation;
        this.mmintermodel_states = mmintermodel_states;
    }

    public String getConfigoperator() {
        return configOperator;
    }

    public void setConfigoperator(String configOperator) {
        this.configOperator = configOperator;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }

    public MMInterModel_StateConfiguration getMmintermodel_stateconfiguration() {
        return mmintermodel_stateconfiguration;
    }

    public void setMmintermodel_stateconfiguration(MMInterModel_StateConfiguration mmintermodel_stateconfiguration) {
        this.mmintermodel_stateconfiguration = mmintermodel_stateconfiguration;
    }
    public List<MMInterModel_State> getMmintermodel_states() {
        return mmintermodel_states;
    }

    public void addMmintermodel_state(Mmintermodel_state mmintermodel_state) {
        this.mmintermodel_states.add(mmintermodel_state);
    }
    public MMInterModel_Model getMmintermodel_model() {
        return mmintermodel_model;
    }

    public void setMmintermodel_model(MMInterModel_Model mmintermodel_model) {
        this.mmintermodel_model = mmintermodel_model;
    }

}