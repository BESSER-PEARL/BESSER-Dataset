





import java.util.List;
import java.util.ArrayList;

public class pivot_Class extends Namespace, Type {

    private String isAbstract;
    private String isInterface;





    private pivot_Class pivot_class;


    public pivot_Class(
        String isAbstract,        String isInterface    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isInterface = isInterface;
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

}