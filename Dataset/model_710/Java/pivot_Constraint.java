





import java.util.List;
import java.util.ArrayList;

public class pivot_Constraint extends NamedElement {

    private String isCallable;





    private pivot_Type pivot_type;


    public pivot_Constraint(
        String isCallable    ) {
        super(
        );
        this.isCallable = isCallable;
    }


    public String getIscallable() {
        return isCallable;
    }

    public void setIscallable(String isCallable) {
        this.isCallable = isCallable;
    }

    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}