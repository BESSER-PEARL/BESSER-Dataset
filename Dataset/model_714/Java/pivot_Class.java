





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends Type, Namespace {

    private String isAbstract;
    private String isActive;
    private String isInterface;





    private pivot_Operation pivot_operation;




    private List<pivot_Class> pivot_classs;


    public pivot_Class(
        String isAbstract,        String isActive,        String isInterface    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isActive = isActive;
        this.isInterface = isInterface;
        this.pivot_classs = new ArrayList<>();
    }

    public pivot_Class(
        String isAbstract,        String isActive,        String isInterface        ArrayList<pivot_Class> pivot_classs    ) {
        this.isAbstract = isAbstract;
        this.isActive = isActive;
        this.isInterface = isInterface;
        this.pivot_classs = pivot_classs;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
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

    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }

}