





import java.util.List;
import java.util.ArrayList;

public class pivot_Type extends TemplateableElement, ParameterableElement, NamedElement {

    private String instanceClassName;





    private pivot_Metaclass pivot_metaclass;




    private List<pivot_Operation> pivot_operations;




    private pivot_LambdaType pivot_lambdatype;




    private pivot_Operation pivot_operation;




    private pivot_Type pivot_type;




    private pivot_LambdaType pivot_lambdatype;




    private pivot_Operation pivot_operation;




    private pivot_Property pivot_property;




    private pivot_LambdaType pivot_lambdatype;




    private pivot_TypeExp pivot_typeexp;




    private List<pivot_Property> pivot_propertys;


    public pivot_Type(
        String instanceClassName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.pivot_operations = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Type(
        String instanceClassName        ArrayList<pivot_Operation> pivot_operations,        ArrayList<pivot_Property> pivot_propertys    ) {
        this.instanceClassName = instanceClassName;
        this.pivot_operations = pivot_operations;
        this.pivot_propertys = pivot_propertys;
    }

    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public pivot_Metaclass getPivot_metaclass() {
        return pivot_metaclass;
    }

    public void setPivot_metaclass(pivot_Metaclass pivot_metaclass) {
        this.pivot_metaclass = pivot_metaclass;
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public pivot_LambdaType getPivot_lambdatype() {
        return pivot_lambdatype;
    }

    public void setPivot_lambdatype(pivot_LambdaType pivot_lambdatype) {
        this.pivot_lambdatype = pivot_lambdatype;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public pivot_LambdaType getPivot_lambdatype() {
        return pivot_lambdatype;
    }

    public void setPivot_lambdatype(pivot_LambdaType pivot_lambdatype) {
        this.pivot_lambdatype = pivot_lambdatype;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_LambdaType getPivot_lambdatype() {
        return pivot_lambdatype;
    }

    public void setPivot_lambdatype(pivot_LambdaType pivot_lambdatype) {
        this.pivot_lambdatype = pivot_lambdatype;
    }
    public pivot_TypeExp getPivot_typeexp() {
        return pivot_typeexp;
    }

    public void setPivot_typeexp(pivot_TypeExp pivot_typeexp) {
        this.pivot_typeexp = pivot_typeexp;
    }
    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }

}