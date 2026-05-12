





import java.util.List;
import java.util.ArrayList;

public class UML2_Operation extends ParameterableElement, MultiplicityElement, TypedElement, BehavioralFeature {

    private boolean isQuery;





    private List<UML2_Constraint> uml2_constraints;




    private UML2_Parameter uml2_parameter;




    private UML2_Constraint uml2_constraint;




    private List<UML2_Operation> uml2_operations;




    private List<UML2_Constraint> uml2_constraints;




    private List<UML2_Parameter> uml2_parameters;


    public UML2_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.uml2_constraints = new ArrayList<>();
        this.uml2_operations = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
    }

    public UML2_Operation(
        boolean isQuery        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_Operation> uml2_operations,        ArrayList<UML2_Constraint> uml2_constraints,        ArrayList<UML2_Parameter> uml2_parameters    ) {
        this.isQuery = isQuery;
        this.uml2_constraints = uml2_constraints;
        this.uml2_operations = uml2_operations;
        this.uml2_constraints = uml2_constraints;
        this.uml2_parameters = uml2_parameters;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public UML2_Parameter getUml2_parameter() {
        return uml2_parameter;
    }

    public void setUml2_parameter(UML2_Parameter uml2_parameter) {
        this.uml2_parameter = uml2_parameter;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
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

}