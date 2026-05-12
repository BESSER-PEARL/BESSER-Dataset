





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends TemplateableElement, Namespace, Type {

    private String isActive;
    private String isInterface;
    private String isAbstract;
    private String instanceClassName;





    private List<pivot_Class> pivot_classs;




    private List<pivot_Operation> pivot_operations;




    private pivot_Operation pivot_operation;


    public pivot_Class(
        String isActive,        String isInterface,        String isAbstract,        String instanceClassName    ) {
        super(
        );
        this.isActive = isActive;
        this.isInterface = isInterface;
        this.isAbstract = isAbstract;
        this.instanceClassName = instanceClassName;
        this.pivot_classs = new ArrayList<>();
        this.pivot_operations = new ArrayList<>();
    }

    public pivot_Class(
        String isActive,        String isInterface,        String isAbstract,        String instanceClassName        ArrayList<pivot_Class> pivot_classs,        ArrayList<pivot_Operation> pivot_operations    ) {
        this.isActive = isActive;
        this.isInterface = isInterface;
        this.isAbstract = isAbstract;
        this.instanceClassName = instanceClassName;
        this.pivot_classs = pivot_classs;
        this.pivot_operations = pivot_operations;
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

    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}