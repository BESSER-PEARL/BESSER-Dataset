





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Node extends GraphElements, RuleNodeTypes, ConditionNodeTypes {

    private String actiontype;



    public henshin_text_Node(
        String actiontype    ) {
        super(
        );
        this.actiontype = actiontype;
    }


    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }


}