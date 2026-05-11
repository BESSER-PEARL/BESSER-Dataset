





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Operation extends BehavioralFeature {

    private boolean isQuery;
    private int upper;
    private boolean isOrdered;
    private boolean isUnique;
    private int lower;





    private Type type;




    private List<Constraint> constraints;




    private List<Constraint> constraints;




    private List<Constraint> constraints;




    private Class class;


    public Classes_Kernel_Operation(
        boolean isQuery,        int upper,        boolean isOrdered,        boolean isUnique,        int lower    ) {
        super(
        );
        this.isQuery = isQuery;
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.lower = lower;
        this.constraints = new ArrayList<>();
        this.constraints = new ArrayList<>();
        this.constraints = new ArrayList<>();
    }

    public Classes_Kernel_Operation(
        boolean isQuery,        int upper,        boolean isOrdered,        boolean isUnique,        int lower        ArrayList<Constraint> constraints,        ArrayList<Constraint> constraints,        ArrayList<Constraint> constraints    ) {
        this.isQuery = isQuery;
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.lower = lower;
        this.constraints = constraints;
        this.constraints = constraints;
        this.constraints = constraints;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
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

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public List<Constraint> getConstraints() {
        return constraints;
    }

    public void addConstraint(Constraint constraint) {
        this.constraints.add(constraint);
    }
    public List<Constraint> getConstraints() {
        return constraints;
    }

    public void addConstraint(Constraint constraint) {
        this.constraints.add(constraint);
    }
    public List<Constraint> getConstraints() {
        return constraints;
    }

    public void addConstraint(Constraint constraint) {
        this.constraints.add(constraint);
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}