





import java.util.List;
import java.util.ArrayList;

public class pivot_Operation extends Feature, Namespace, TemplateableElement {

    private String isValidating;
    private String isInvalidating;
    private String isTypeof;





    private pivot_CallOperationAction pivot_calloperationaction;




    private pivot_Constraint pivot_constraint;




    private pivot_Precedence pivot_precedence;




    private pivot_Constraint pivot_constraint;




    private pivot_MessageType pivot_messagetype;




    private List<pivot_Constraint> pivot_constraints;




    private List<pivot_Type> pivot_types;




    private List<pivot_Operation> pivot_operations;




    private List<pivot_Constraint> pivot_constraints;


    public pivot_Operation(
        String isValidating,        String isInvalidating,        String isTypeof    ) {
        super(
        );
        this.isValidating = isValidating;
        this.isInvalidating = isInvalidating;
        this.isTypeof = isTypeof;
        this.pivot_constraints = new ArrayList<>();
        this.pivot_types = new ArrayList<>();
        this.pivot_operations = new ArrayList<>();
        this.pivot_constraints = new ArrayList<>();
    }

    public pivot_Operation(
        String isValidating,        String isInvalidating,        String isTypeof        ArrayList<pivot_Constraint> pivot_constraints,        ArrayList<pivot_Type> pivot_types,        ArrayList<pivot_Operation> pivot_operations,        ArrayList<pivot_Constraint> pivot_constraints    ) {
        this.isValidating = isValidating;
        this.isInvalidating = isInvalidating;
        this.isTypeof = isTypeof;
        this.pivot_constraints = pivot_constraints;
        this.pivot_types = pivot_types;
        this.pivot_operations = pivot_operations;
        this.pivot_constraints = pivot_constraints;
    }

    public String getIsvalidating() {
        return isValidating;
    }

    public void setIsvalidating(String isValidating) {
        this.isValidating = isValidating;
    }
    public String getIsinvalidating() {
        return isInvalidating;
    }

    public void setIsinvalidating(String isInvalidating) {
        this.isInvalidating = isInvalidating;
    }
    public String getIstypeof() {
        return isTypeof;
    }

    public void setIstypeof(String isTypeof) {
        this.isTypeof = isTypeof;
    }

    public pivot_CallOperationAction getPivot_calloperationaction() {
        return pivot_calloperationaction;
    }

    public void setPivot_calloperationaction(pivot_CallOperationAction pivot_calloperationaction) {
        this.pivot_calloperationaction = pivot_calloperationaction;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Precedence getPivot_precedence() {
        return pivot_precedence;
    }

    public void setPivot_precedence(pivot_Precedence pivot_precedence) {
        this.pivot_precedence = pivot_precedence;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_MessageType getPivot_messagetype() {
        return pivot_messagetype;
    }

    public void setPivot_messagetype(pivot_MessageType pivot_messagetype) {
        this.pivot_messagetype = pivot_messagetype;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }

}