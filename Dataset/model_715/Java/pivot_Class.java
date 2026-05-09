





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends Type, TemplateableElement, Namespace {

    private String isActive;
    private String isInterface;
    private String isAbstract;
    private String instanceClassName;





    private pivot_Operation pivot_operation;




    private List<pivot_Operation> pivot_operations;




    private pivot_CompleteClass pivot_completeclass;




    private List<pivot_Behavior> pivot_behaviors;




    private List<pivot_Constraint> pivot_constraints;




    private pivot_InstanceSpecification pivot_instancespecification;




    private pivot_DataType pivot_datatype;




    private List<pivot_Class> pivot_classs;


    public pivot_Class(
        String isActive,        String isInterface,        String isAbstract,        String instanceClassName    ) {
        super(
        );
        this.isActive = isActive;
        this.isInterface = isInterface;
        this.isAbstract = isAbstract;
        this.instanceClassName = instanceClassName;
        this.pivot_operations = new ArrayList<>();
        this.pivot_behaviors = new ArrayList<>();
        this.pivot_constraints = new ArrayList<>();
        this.pivot_classs = new ArrayList<>();
    }

    public pivot_Class(
        String isActive,        String isInterface,        String isAbstract,        String instanceClassName        ArrayList<pivot_Operation> pivot_operations,        ArrayList<pivot_Behavior> pivot_behaviors,        ArrayList<pivot_Constraint> pivot_constraints,        ArrayList<pivot_Class> pivot_classs    ) {
        this.isActive = isActive;
        this.isInterface = isInterface;
        this.isAbstract = isAbstract;
        this.instanceClassName = instanceClassName;
        this.pivot_operations = pivot_operations;
        this.pivot_behaviors = pivot_behaviors;
        this.pivot_constraints = pivot_constraints;
        this.pivot_classs = pivot_classs;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }
    public String getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(String isInterface) {
        this.isInterface = isInterface;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public pivot_CompleteClass getPivot_completeclass() {
        return pivot_completeclass;
    }

    public void setPivot_completeclass(pivot_CompleteClass pivot_completeclass) {
        this.pivot_completeclass = pivot_completeclass;
    }
    public List<pivot_Behavior> getPivot_behaviors() {
        return pivot_behaviors;
    }

    public void addPivot_behavior(Pivot_behavior pivot_behavior) {
        this.pivot_behaviors.add(pivot_behavior);
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }
    public pivot_DataType getPivot_datatype() {
        return pivot_datatype;
    }

    public void setPivot_datatype(pivot_DataType pivot_datatype) {
        this.pivot_datatype = pivot_datatype;
    }
    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }

}