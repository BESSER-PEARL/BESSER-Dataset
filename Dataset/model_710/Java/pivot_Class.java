





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends Type, Namespace {

    private String isAbstract;
    private String isInterface;





    private pivot_Property pivot_property;




    private List<pivot_Behavior> pivot_behaviors;




    private pivot_Operation pivot_operation;


    public pivot_Class(
        String isAbstract,        String isInterface    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isInterface = isInterface;
        this.pivot_behaviors = new ArrayList<>();
    }

    public pivot_Class(
        String isAbstract,        String isInterface        ArrayList<pivot_Behavior> pivot_behaviors    ) {
        this.isAbstract = isAbstract;
        this.isInterface = isInterface;
        this.pivot_behaviors = pivot_behaviors;
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

    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public List<pivot_Behavior> getPivot_behaviors() {
        return pivot_behaviors;
    }

    public void addPivot_behavior(Pivot_behavior pivot_behavior) {
        this.pivot_behaviors.add(pivot_behavior);
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}