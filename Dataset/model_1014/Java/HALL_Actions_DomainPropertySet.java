





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_DomainPropertySet extends ActionMessageExpressionElement {

    private String name;





    private Actions_ActionMessageExpressionElement actions_actionmessageexpressionelement;


    public HALL_Actions_DomainPropertySet(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Actions_ActionMessageExpressionElement getActions_actionmessageexpressionelement() {
        return actions_actionmessageexpressionelement;
    }

    public void setActions_actionmessageexpressionelement(Actions_ActionMessageExpressionElement actions_actionmessageexpressionelement) {
        this.actions_actionmessageexpressionelement = actions_actionmessageexpressionelement;
    }

}