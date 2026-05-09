





import java.util.List;
import java.util.ArrayList;

public class pivot_Operation extends TemplateableElement, Namespace, ParameterableElement, Feature {

    private String isInvalidating;
    private String isValidating;





    private pivot_CallOperationAction pivot_calloperationaction;




    private pivot_Type pivot_type;




    private List<pivot_Constraint> pivot_constraints;




    private List<pivot_Operation> pivot_operations;




    private pivot_Precedence pivot_precedence;




    private List<pivot_Type> pivot_types;




    private pivot_Type pivot_type;




    private List<pivot_Constraint> pivot_constraints;


    public pivot_Operation(
        String isInvalidating,        String isValidating    ) {
        super(
        );
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
        this.pivot_constraints = new ArrayList<>();
        this.pivot_operations = new ArrayList<>();
        this.pivot_types = new ArrayList<>();
        this.pivot_constraints = new ArrayList<>();
    }

    public pivot_Operation(
        String isInvalidating,        String isValidating        ArrayList<pivot_Constraint> pivot_constraints,        ArrayList<pivot_Operation> pivot_operations,        ArrayList<pivot_Type> pivot_types,        ArrayList<pivot_Constraint> pivot_constraints    ) {
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
        this.pivot_constraints = pivot_constraints;
        this.pivot_operations = pivot_operations;
        this.pivot_types = pivot_types;
        this.pivot_constraints = pivot_constraints;
    }

    public String getIsinvalidating() {
        return isInvalidating;
    }

    public void setIsinvalidating(String isInvalidating) {
        this.isInvalidating = isInvalidating;
    }
    public String getIsvalidating() {
        return isValidating;
    }

    public void setIsvalidating(String isValidating) {
        this.isValidating = isValidating;
    }

    public pivot_CallOperationAction getPivot_calloperationaction() {
        return pivot_calloperationaction;
    }

    public void setPivot_calloperationaction(pivot_CallOperationAction pivot_calloperationaction) {
        this.pivot_calloperationaction = pivot_calloperationaction;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public pivot_Precedence getPivot_precedence() {
        return pivot_precedence;
    }

    public void setPivot_precedence(pivot_Precedence pivot_precedence) {
        this.pivot_precedence = pivot_precedence;
    }
    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }

}