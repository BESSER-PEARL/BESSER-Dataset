





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_Enable extends ActionMessageExpressionElement {






    private List<Actions_ActionMessageExpressionElement> actions_actionmessageexpressionelements;


    public HALL_Actions_Enable(
    ) {
        super(
        );
        this.actions_actionmessageexpressionelements = new ArrayList<>();
    }

    public HALL_Actions_Enable(
        ArrayList<Actions_ActionMessageExpressionElement> actions_actionmessageexpressionelements    ) {
        this.actions_actionmessageexpressionelements = actions_actionmessageexpressionelements;
    }


    public List<Actions_ActionMessageExpressionElement> getActions_actionmessageexpressionelements() {
        return actions_actionmessageexpressionelements;
    }

    public void addActions_actionmessageexpressionelement(Actions_actionmessageexpressionelement actions_actionmessageexpressionelement) {
        this.actions_actionmessageexpressionelements.add(actions_actionmessageexpressionelement);
    }

}