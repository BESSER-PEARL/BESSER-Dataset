





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_ActionMessageExpression  {






    private MessageTransition messagetransition;




    private List<Actions_ActionMessageExpressionElement> actions_actionmessageexpressionelements;


    public HALL_Actions_ActionMessageExpression(
    ) {
        this.actions_actionmessageexpressionelements = new ArrayList<>();
    }

    public HALL_Actions_ActionMessageExpression(
        ArrayList<Actions_ActionMessageExpressionElement> actions_actionmessageexpressionelements    ) {
        this.actions_actionmessageexpressionelements = actions_actionmessageexpressionelements;
    }


    public MessageTransition getMessagetransition() {
        return messagetransition;
    }

    public void setMessagetransition(MessageTransition messagetransition) {
        this.messagetransition = messagetransition;
    }
    public List<Actions_ActionMessageExpressionElement> getActions_actionmessageexpressionelements() {
        return actions_actionmessageexpressionelements;
    }

    public void addActions_actionmessageexpressionelement(Actions_actionmessageexpressionelement actions_actionmessageexpressionelement) {
        this.actions_actionmessageexpressionelements.add(actions_actionmessageexpressionelement);
    }

}