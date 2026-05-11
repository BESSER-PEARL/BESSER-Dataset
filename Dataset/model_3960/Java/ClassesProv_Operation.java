





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Operation extends BehavioralFeature {

    private boolean isUnique;
    private int lower;
    private int upper;
    private boolean isOrdered;
    private boolean isQuery;





    private List<ClassesProv_Constraint> classesprov_constraints;




    private List<ClassesProv_Constraint> classesprov_constraints;




    private ClassesProv_Interface classesprov_interface;




    private List<ClassesProv_Constraint> classesprov_constraints;




    private ClassesProv_DataType classesprov_datatype;




    private ClassesProv_Class classesprov_class;




    private ClassesProv_DataType classesprov_datatype;




    private ClassesProv_Interface classesprov_interface;




    private ClassesProv_Type classesprov_type;




    private ClassesProv_Class classesprov_class;


    public ClassesProv_Operation(
        boolean isUnique,        int lower,        int upper,        boolean isOrdered,        boolean isQuery    ) {
        super(
        );
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.isQuery = isQuery;
        this.classesprov_constraints = new ArrayList<>();
        this.classesprov_constraints = new ArrayList<>();
        this.classesprov_constraints = new ArrayList<>();
    }

    public ClassesProv_Operation(
        boolean isUnique,        int lower,        int upper,        boolean isOrdered,        boolean isQuery        ArrayList<ClassesProv_Constraint> classesprov_constraints,        ArrayList<ClassesProv_Constraint> classesprov_constraints,        ArrayList<ClassesProv_Constraint> classesprov_constraints    ) {
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.isQuery = isQuery;
        this.classesprov_constraints = classesprov_constraints;
        this.classesprov_constraints = classesprov_constraints;
        this.classesprov_constraints = classesprov_constraints;
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
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public List<ClassesProv_Constraint> getClassesprov_constraints() {
        return classesprov_constraints;
    }

    public void addClassesprov_constraint(Classesprov_constraint classesprov_constraint) {
        this.classesprov_constraints.add(classesprov_constraint);
    }
    public List<ClassesProv_Constraint> getClassesprov_constraints() {
        return classesprov_constraints;
    }

    public void addClassesprov_constraint(Classesprov_constraint classesprov_constraint) {
        this.classesprov_constraints.add(classesprov_constraint);
    }
    public ClassesProv_Interface getClassesprov_interface() {
        return classesprov_interface;
    }

    public void setClassesprov_interface(ClassesProv_Interface classesprov_interface) {
        this.classesprov_interface = classesprov_interface;
    }
    public List<ClassesProv_Constraint> getClassesprov_constraints() {
        return classesprov_constraints;
    }

    public void addClassesprov_constraint(Classesprov_constraint classesprov_constraint) {
        this.classesprov_constraints.add(classesprov_constraint);
    }
    public ClassesProv_DataType getClassesprov_datatype() {
        return classesprov_datatype;
    }

    public void setClassesprov_datatype(ClassesProv_DataType classesprov_datatype) {
        this.classesprov_datatype = classesprov_datatype;
    }
    public ClassesProv_Class getClassesprov_class() {
        return classesprov_class;
    }

    public void setClassesprov_class(ClassesProv_Class classesprov_class) {
        this.classesprov_class = classesprov_class;
    }
    public ClassesProv_DataType getClassesprov_datatype() {
        return classesprov_datatype;
    }

    public void setClassesprov_datatype(ClassesProv_DataType classesprov_datatype) {
        this.classesprov_datatype = classesprov_datatype;
    }
    public ClassesProv_Interface getClassesprov_interface() {
        return classesprov_interface;
    }

    public void setClassesprov_interface(ClassesProv_Interface classesprov_interface) {
        this.classesprov_interface = classesprov_interface;
    }
    public ClassesProv_Type getClassesprov_type() {
        return classesprov_type;
    }

    public void setClassesprov_type(ClassesProv_Type classesprov_type) {
        this.classesprov_type = classesprov_type;
    }
    public ClassesProv_Class getClassesprov_class() {
        return classesprov_class;
    }

    public void setClassesprov_class(ClassesProv_Class classesprov_class) {
        this.classesprov_class = classesprov_class;
    }

}