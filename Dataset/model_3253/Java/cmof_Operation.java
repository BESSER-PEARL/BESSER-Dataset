





import java.util.List;
import java.util.ArrayList;

public class cmof_Operation extends TypedElement, MultiplicityElement, BehavioralFeature {

    private boolean isQuery;





    private cmof_DataType cmof_datatype;




    private cmof_Class cmof_class;




    private cmof_Class cmof_class;




    private List<cmof_Constraint> cmof_constraints;




    private cmof_DataType cmof_datatype;




    private List<cmof_Operation> cmof_operations;




    private List<cmof_Constraint> cmof_constraints;




    private List<cmof_Constraint> cmof_constraints;


    public cmof_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.cmof_constraints = new ArrayList<>();
        this.cmof_operations = new ArrayList<>();
        this.cmof_constraints = new ArrayList<>();
        this.cmof_constraints = new ArrayList<>();
    }

    public cmof_Operation(
        boolean isQuery        ArrayList<cmof_Constraint> cmof_constraints,        ArrayList<cmof_Operation> cmof_operations,        ArrayList<cmof_Constraint> cmof_constraints,        ArrayList<cmof_Constraint> cmof_constraints    ) {
        this.isQuery = isQuery;
        this.cmof_constraints = cmof_constraints;
        this.cmof_operations = cmof_operations;
        this.cmof_constraints = cmof_constraints;
        this.cmof_constraints = cmof_constraints;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public cmof_DataType getCmof_datatype() {
        return cmof_datatype;
    }

    public void setCmof_datatype(cmof_DataType cmof_datatype) {
        this.cmof_datatype = cmof_datatype;
    }
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }
    public List<cmof_Constraint> getCmof_constraints() {
        return cmof_constraints;
    }

    public void addCmof_constraint(Cmof_constraint cmof_constraint) {
        this.cmof_constraints.add(cmof_constraint);
    }
    public cmof_DataType getCmof_datatype() {
        return cmof_datatype;
    }

    public void setCmof_datatype(cmof_DataType cmof_datatype) {
        this.cmof_datatype = cmof_datatype;
    }
    public List<cmof_Operation> getCmof_operations() {
        return cmof_operations;
    }

    public void addCmof_operation(Cmof_operation cmof_operation) {
        this.cmof_operations.add(cmof_operation);
    }
    public List<cmof_Constraint> getCmof_constraints() {
        return cmof_constraints;
    }

    public void addCmof_constraint(Cmof_constraint cmof_constraint) {
        this.cmof_constraints.add(cmof_constraint);
    }
    public List<cmof_Constraint> getCmof_constraints() {
        return cmof_constraints;
    }

    public void addCmof_constraint(Cmof_constraint cmof_constraint) {
        this.cmof_constraints.add(cmof_constraint);
    }

}