





import java.util.List;
import java.util.ArrayList;

public class nuSMV_AssignConstraintElement extends ModuleElement {

    private String assign;



    public nuSMV_AssignConstraintElement(
        String assign    ) {
        super(
        );
        this.assign = assign;
    }


    public String getAssign() {
        return assign;
    }

    public void setAssign(String assign) {
        this.assign = assign;
    }


}