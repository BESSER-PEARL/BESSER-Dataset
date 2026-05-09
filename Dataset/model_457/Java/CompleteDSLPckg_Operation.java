





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Operation extends BehavioralFeature {

    private boolean isOrdered;
    private boolean isUnique;
    private int lower;
    private int upper;
    private boolean isQuery;





    private CompleteDSLPckg_Interface completedslpckg_interface;




    private CompleteDSLPckg_DataType completedslpckg_datatype;




    private CompleteDSLPckg_Interface completedslpckg_interface;




    private CompleteDSLPckg_Class completedslpckg_class;




    private CompleteDSLPckg_Type completedslpckg_type;




    private List<CompleteDSLPckg_Constraint> completedslpckg_constraints;




    private List<CompleteDSLPckg_Constraint> completedslpckg_constraints;




    private CompleteDSLPckg_DataType completedslpckg_datatype;




    private CompleteDSLPckg_Class completedslpckg_class;




    private List<CompleteDSLPckg_Constraint> completedslpckg_constraints;




    private CompleteDSLPckg_Artifact completedslpckg_artifact;


    public CompleteDSLPckg_Operation(
        boolean isOrdered,        boolean isUnique,        int lower,        int upper,        boolean isQuery    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isQuery = isQuery;
        this.completedslpckg_constraints = new ArrayList<>();
        this.completedslpckg_constraints = new ArrayList<>();
        this.completedslpckg_constraints = new ArrayList<>();
    }

    public CompleteDSLPckg_Operation(
        boolean isOrdered,        boolean isUnique,        int lower,        int upper,        boolean isQuery        ArrayList<CompleteDSLPckg_Constraint> completedslpckg_constraints,        ArrayList<CompleteDSLPckg_Constraint> completedslpckg_constraints,        ArrayList<CompleteDSLPckg_Constraint> completedslpckg_constraints    ) {
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isQuery = isQuery;
        this.completedslpckg_constraints = completedslpckg_constraints;
        this.completedslpckg_constraints = completedslpckg_constraints;
        this.completedslpckg_constraints = completedslpckg_constraints;
    }

    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public CompleteDSLPckg_Interface getCompletedslpckg_interface() {
        return completedslpckg_interface;
    }

    public void setCompletedslpckg_interface(CompleteDSLPckg_Interface completedslpckg_interface) {
        this.completedslpckg_interface = completedslpckg_interface;
    }
    public CompleteDSLPckg_DataType getCompletedslpckg_datatype() {
        return completedslpckg_datatype;
    }

    public void setCompletedslpckg_datatype(CompleteDSLPckg_DataType completedslpckg_datatype) {
        this.completedslpckg_datatype = completedslpckg_datatype;
    }
    public CompleteDSLPckg_Interface getCompletedslpckg_interface() {
        return completedslpckg_interface;
    }

    public void setCompletedslpckg_interface(CompleteDSLPckg_Interface completedslpckg_interface) {
        this.completedslpckg_interface = completedslpckg_interface;
    }
    public CompleteDSLPckg_Class getCompletedslpckg_class() {
        return completedslpckg_class;
    }

    public void setCompletedslpckg_class(CompleteDSLPckg_Class completedslpckg_class) {
        this.completedslpckg_class = completedslpckg_class;
    }
    public CompleteDSLPckg_Type getCompletedslpckg_type() {
        return completedslpckg_type;
    }

    public void setCompletedslpckg_type(CompleteDSLPckg_Type completedslpckg_type) {
        this.completedslpckg_type = completedslpckg_type;
    }
    public List<CompleteDSLPckg_Constraint> getCompletedslpckg_constraints() {
        return completedslpckg_constraints;
    }

    public void addCompletedslpckg_constraint(Completedslpckg_constraint completedslpckg_constraint) {
        this.completedslpckg_constraints.add(completedslpckg_constraint);
    }
    public List<CompleteDSLPckg_Constraint> getCompletedslpckg_constraints() {
        return completedslpckg_constraints;
    }

    public void addCompletedslpckg_constraint(Completedslpckg_constraint completedslpckg_constraint) {
        this.completedslpckg_constraints.add(completedslpckg_constraint);
    }
    public CompleteDSLPckg_DataType getCompletedslpckg_datatype() {
        return completedslpckg_datatype;
    }

    public void setCompletedslpckg_datatype(CompleteDSLPckg_DataType completedslpckg_datatype) {
        this.completedslpckg_datatype = completedslpckg_datatype;
    }
    public CompleteDSLPckg_Class getCompletedslpckg_class() {
        return completedslpckg_class;
    }

    public void setCompletedslpckg_class(CompleteDSLPckg_Class completedslpckg_class) {
        this.completedslpckg_class = completedslpckg_class;
    }
    public List<CompleteDSLPckg_Constraint> getCompletedslpckg_constraints() {
        return completedslpckg_constraints;
    }

    public void addCompletedslpckg_constraint(Completedslpckg_constraint completedslpckg_constraint) {
        this.completedslpckg_constraints.add(completedslpckg_constraint);
    }
    public CompleteDSLPckg_Artifact getCompletedslpckg_artifact() {
        return completedslpckg_artifact;
    }

    public void setCompletedslpckg_artifact(CompleteDSLPckg_Artifact completedslpckg_artifact) {
        this.completedslpckg_artifact = completedslpckg_artifact;
    }

}