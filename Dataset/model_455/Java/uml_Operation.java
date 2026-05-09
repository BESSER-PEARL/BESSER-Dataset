





import java.util.List;
import java.util.ArrayList;

public class uml_Operation extends BehavioralFeature, TemplateableElement, ParameterableElement {

    private String isQuery;
    private String isUnique;
    private String lower;
    private String upper;
    private String isOrdered;





    private List<uml_Constraint> uml_constraints;




    private List<uml_Constraint> uml_constraints;




    private List<uml_Operation> uml_operations;




    private uml_Constraint uml_constraint;




    private uml_DataType uml_datatype;




    private uml_DataType uml_datatype;




    private uml_Type uml_type;


    public uml_Operation(
        String isQuery,        String isUnique,        String lower,        String upper,        String isOrdered    ) {
        super(
        );
        this.isQuery = isQuery;
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.uml_constraints = new ArrayList<>();
        this.uml_constraints = new ArrayList<>();
        this.uml_operations = new ArrayList<>();
    }

    public uml_Operation(
        String isQuery,        String isUnique,        String lower,        String upper,        String isOrdered        ArrayList<uml_Constraint> uml_constraints,        ArrayList<uml_Constraint> uml_constraints,        ArrayList<uml_Operation> uml_operations    ) {
        this.isQuery = isQuery;
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.uml_constraints = uml_constraints;
        this.uml_constraints = uml_constraints;
        this.uml_operations = uml_operations;
    }

    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
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
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }

    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public List<uml_Operation> getUml_operations() {
        return uml_operations;
    }

    public void addUml_operation(Uml_operation uml_operation) {
        this.uml_operations.add(uml_operation);
    }
    public uml_Constraint getUml_constraint() {
        return uml_constraint;
    }

    public void setUml_constraint(uml_Constraint uml_constraint) {
        this.uml_constraint = uml_constraint;
    }
    public uml_DataType getUml_datatype() {
        return uml_datatype;
    }

    public void setUml_datatype(uml_DataType uml_datatype) {
        this.uml_datatype = uml_datatype;
    }
    public uml_DataType getUml_datatype() {
        return uml_datatype;
    }

    public void setUml_datatype(uml_DataType uml_datatype) {
        this.uml_datatype = uml_datatype;
    }
    public uml_Type getUml_type() {
        return uml_type;
    }

    public void setUml_type(uml_Type uml_type) {
        this.uml_type = uml_type;
    }

}