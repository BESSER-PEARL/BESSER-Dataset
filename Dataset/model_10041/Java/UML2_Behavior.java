





import java.util.List;
import java.util.ArrayList;

public class UML2_Behavior extends Class {

    private boolean isReentrant;





    private List<UML2_Constraint> uml2_constraints;




    private List<UML2_ParameterSet> uml2_parametersets;




    private UML2_OpaqueExpression uml2_opaqueexpression;




    private List<UML2_Constraint> uml2_constraints;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private UML2_Behavior uml2_behavior;


    public UML2_Behavior(
        boolean isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.uml2_constraints = new ArrayList<>();
        this.uml2_parametersets = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
    }

    public UML2_Behavior(
        boolean isReentrant        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_ParameterSet> uml2_parametersets,        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters    ) {
        this.isReentrant = isReentrant;
        this.uml2_constraints = uml2_constraints;
        this.uml2_parametersets = uml2_parametersets;
        this.uml2_constraints = uml2_constraints;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
    }

    public boolean getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(boolean isReentrant) {
        this.isReentrant = isReentrant;
    }

    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public List<UML2_ParameterSet> getUml2_parametersets() {
        return uml2_parametersets;
    }

    public void addUml2_parameterset(Uml2_parameterset uml2_parameterset) {
        this.uml2_parametersets.add(uml2_parameterset);
    }
    public UML2_OpaqueExpression getUml2_opaqueexpression() {
        return uml2_opaqueexpression;
    }

    public void setUml2_opaqueexpression(UML2_OpaqueExpression uml2_opaqueexpression) {
        this.uml2_opaqueexpression = uml2_opaqueexpression;
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }

}