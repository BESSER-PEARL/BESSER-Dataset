





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Behavior extends Class {

    private String specification;
    private String postcondition;
    private String precondition;
    private String redefinedBahavior;
    private String isReentrant;
    private String context;





    private List<UMLModel_Parameter> umlmodel_parameters;




    private UMLModel_State umlmodel_state;




    private UMLModel_State umlmodel_state;




    private List<UMLModel_ParameterSet> umlmodel_parametersets;




    private UMLModel_State umlmodel_state;




    private UMLModel_Transition umlmodel_transition;


    public UMLModel_Behavior(
        String specification,        String postcondition,        String precondition,        String redefinedBahavior,        String isReentrant,        String context    ) {
        super(
        );
        this.specification = specification;
        this.postcondition = postcondition;
        this.precondition = precondition;
        this.redefinedBahavior = redefinedBahavior;
        this.isReentrant = isReentrant;
        this.context = context;
        this.umlmodel_parameters = new ArrayList<>();
        this.umlmodel_parametersets = new ArrayList<>();
    }

    public UMLModel_Behavior(
        String specification,        String postcondition,        String precondition,        String redefinedBahavior,        String isReentrant,        String context        ArrayList<UMLModel_Parameter> umlmodel_parameters,        ArrayList<UMLModel_ParameterSet> umlmodel_parametersets    ) {
        this.specification = specification;
        this.postcondition = postcondition;
        this.precondition = precondition;
        this.redefinedBahavior = redefinedBahavior;
        this.isReentrant = isReentrant;
        this.context = context;
        this.umlmodel_parameters = umlmodel_parameters;
        this.umlmodel_parametersets = umlmodel_parametersets;
    }

    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getRedefinedbahavior() {
        return redefinedBahavior;
    }

    public void setRedefinedbahavior(String redefinedBahavior) {
        this.redefinedBahavior = redefinedBahavior;
    }
    public String getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(String isReentrant) {
        this.isReentrant = isReentrant;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public List<UMLModel_Parameter> getUmlmodel_parameters() {
        return umlmodel_parameters;
    }

    public void addUmlmodel_parameter(Umlmodel_parameter umlmodel_parameter) {
        this.umlmodel_parameters.add(umlmodel_parameter);
    }
    public UMLModel_State getUmlmodel_state() {
        return umlmodel_state;
    }

    public void setUmlmodel_state(UMLModel_State umlmodel_state) {
        this.umlmodel_state = umlmodel_state;
    }
    public UMLModel_State getUmlmodel_state() {
        return umlmodel_state;
    }

    public void setUmlmodel_state(UMLModel_State umlmodel_state) {
        this.umlmodel_state = umlmodel_state;
    }
    public List<UMLModel_ParameterSet> getUmlmodel_parametersets() {
        return umlmodel_parametersets;
    }

    public void addUmlmodel_parameterset(Umlmodel_parameterset umlmodel_parameterset) {
        this.umlmodel_parametersets.add(umlmodel_parameterset);
    }
    public UMLModel_State getUmlmodel_state() {
        return umlmodel_state;
    }

    public void setUmlmodel_state(UMLModel_State umlmodel_state) {
        this.umlmodel_state = umlmodel_state;
    }
    public UMLModel_Transition getUmlmodel_transition() {
        return umlmodel_transition;
    }

    public void setUmlmodel_transition(UMLModel_Transition umlmodel_transition) {
        this.umlmodel_transition = umlmodel_transition;
    }

}