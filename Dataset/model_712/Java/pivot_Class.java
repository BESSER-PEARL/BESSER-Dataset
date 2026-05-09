





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends Type, Namespace {

    private String isInterface;
    private String isAbstract;





    private pivot_Class pivot_class;




    private pivot_Operation pivot_operation;




    private pivot_Property pivot_property;




    private List<pivot_Behavior> pivot_behaviors;


    public pivot_Class(
        String isInterface,        String isAbstract    ) {
        super(
        );
        this.isInterface = isInterface;
        this.isAbstract = isAbstract;
        this.pivot_behaviors = new ArrayList<>();
    }

    public pivot_Class(
        String isInterface,        String isAbstract        ArrayList<pivot_Behavior> pivot_behaviors    ) {
        this.isInterface = isInterface;
        this.isAbstract = isAbstract;
        this.pivot_behaviors = pivot_behaviors;
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

    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
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
    public List<pivot_Behavior> getPivot_behaviors() {
        return pivot_behaviors;
    }

    public void addPivot_behavior(Pivot_behavior pivot_behavior) {
        this.pivot_behaviors.add(pivot_behavior);
    }

}