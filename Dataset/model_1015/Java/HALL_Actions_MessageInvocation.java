





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_MessageInvocation extends ActionMessageExpressionElement {

    private String name;
    private boolean isTopDown;





    private Actions_ActionMessageExpressionElement actions_actionmessageexpressionelement;


    public HALL_Actions_MessageInvocation(
        String name,        boolean isTopDown    ) {
        super(
        );
        this.name = name;
        this.isTopDown = isTopDown;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIstopdown() {
        return isTopDown;
    }

    public void setIstopdown(boolean isTopDown) {
        this.isTopDown = isTopDown;
    }

    public Actions_ActionMessageExpressionElement getActions_actionmessageexpressionelement() {
        return actions_actionmessageexpressionelement;
    }

    public void setActions_actionmessageexpressionelement(Actions_ActionMessageExpressionElement actions_actionmessageexpressionelement) {
        this.actions_actionmessageexpressionelement = actions_actionmessageexpressionelement;
    }

}