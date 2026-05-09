





import java.util.List;
import java.util.ArrayList;

public class org_structure_ModelTransformation extends MultiplicityElement {

    private String isAbstract;





    private behavior_Expression behavior_expression;


    public org_structure_ModelTransformation(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }

}