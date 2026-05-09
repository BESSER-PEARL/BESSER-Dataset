





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends Type, Namespace, TemplateableElement {

    private String instanceClassName;
    private String isActive;
    private String isAbstract;
    private String isInterface;





    private pivot_Class pivot_class;




    private List<pivot_Operation> pivot_operations;




    private pivot_TemplateParameter pivot_templateparameter;




    private pivot_CompleteClass pivot_completeclass;




    private pivot_InstanceSpecification pivot_instancespecification;




    private pivot_Property pivot_property;




    private pivot_DataType pivot_datatype;




    private pivot_Operation pivot_operation;




    private List<pivot_Constraint> pivot_constraints;




    private List<pivot_Property> pivot_propertys;




    private List<pivot_Behavior> pivot_behaviors;


    public pivot_Class(
        String instanceClassName,        String isActive,        String isAbstract,        String isInterface    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.isActive = isActive;
        this.isAbstract = isAbstract;
        this.isInterface = isInterface;
        this.pivot_operations = new ArrayList<>();
        this.pivot_constraints = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
        this.pivot_behaviors = new ArrayList<>();
    }

    public pivot_Class(
        String instanceClassName,        String isActive,        String isAbstract,        String isInterface        ArrayList<pivot_Operation> pivot_operations,        ArrayList<pivot_Constraint> pivot_constraints,        ArrayList<pivot_Property> pivot_propertys,        ArrayList<pivot_Behavior> pivot_behaviors    ) {
        this.instanceClassName = instanceClassName;
        this.isActive = isActive;
        this.isAbstract = isAbstract;
        this.isInterface = isInterface;
        this.pivot_operations = pivot_operations;
        this.pivot_constraints = pivot_constraints;
        this.pivot_propertys = pivot_propertys;
        this.pivot_behaviors = pivot_behaviors;
    }

    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }
    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(String isInterface) {
        this.isInterface = isInterface;
    }

    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public pivot_TemplateParameter getPivot_templateparameter() {
        return pivot_templateparameter;
    }

    public void setPivot_templateparameter(pivot_TemplateParameter pivot_templateparameter) {
        this.pivot_templateparameter = pivot_templateparameter;
    }
    public pivot_CompleteClass getPivot_completeclass() {
        return pivot_completeclass;
    }

    public void setPivot_completeclass(pivot_CompleteClass pivot_completeclass) {
        this.pivot_completeclass = pivot_completeclass;
    }
    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_DataType getPivot_datatype() {
        return pivot_datatype;
    }

    public void setPivot_datatype(pivot_DataType pivot_datatype) {
        this.pivot_datatype = pivot_datatype;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public List<pivot_Behavior> getPivot_behaviors() {
        return pivot_behaviors;
    }

    public void addPivot_behavior(Pivot_behavior pivot_behavior) {
        this.pivot_behaviors.add(pivot_behavior);
    }

}