





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Operation extends BehavioralFeature, TemplateableElement, ParameterableElement {

    private String isUnique;
    private String isOrdered;
    private String lower;
    private String upper;
    private String isQuery;





    private List<uml3_0_0_Constraint> uml3_0_0_constraints;




    private List<uml3_0_0_Constraint> uml3_0_0_constraints;




    private uml3_0_0_Type uml3_0_0_type;




    private List<uml3_0_0_Operation> uml3_0_0_operations;




    private uml3_0_0_Constraint uml3_0_0_constraint;


    public uml3_0_0_Operation(
        String isUnique,        String isOrdered,        String lower,        String upper,        String isQuery    ) {
        super(
        );
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.upper = upper;
        this.isQuery = isQuery;
        this.uml3_0_0_constraints = new ArrayList<>();
        this.uml3_0_0_constraints = new ArrayList<>();
        this.uml3_0_0_operations = new ArrayList<>();
    }

    public uml3_0_0_Operation(
        String isUnique,        String isOrdered,        String lower,        String upper,        String isQuery        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints,        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints,        ArrayList<uml3_0_0_Operation> uml3_0_0_operations    ) {
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.upper = upper;
        this.isQuery = isQuery;
        this.uml3_0_0_constraints = uml3_0_0_constraints;
        this.uml3_0_0_constraints = uml3_0_0_constraints;
        this.uml3_0_0_operations = uml3_0_0_operations;
    }

    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }

    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }
    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }
    public uml3_0_0_Type getUml3_0_0_type() {
        return uml3_0_0_type;
    }

    public void setUml3_0_0_type(uml3_0_0_Type uml3_0_0_type) {
        this.uml3_0_0_type = uml3_0_0_type;
    }
    public List<uml3_0_0_Operation> getUml3_0_0_operations() {
        return uml3_0_0_operations;
    }

    public void addUml3_0_0_operation(Uml3_0_0_operation uml3_0_0_operation) {
        this.uml3_0_0_operations.add(uml3_0_0_operation);
    }
    public uml3_0_0_Constraint getUml3_0_0_constraint() {
        return uml3_0_0_constraint;
    }

    public void setUml3_0_0_constraint(uml3_0_0_Constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraint = uml3_0_0_constraint;
    }

}