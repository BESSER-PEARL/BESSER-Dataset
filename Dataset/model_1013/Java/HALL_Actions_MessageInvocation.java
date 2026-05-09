





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_MessageInvocation extends ActionMessageExpression {

    private boolean isTopDown;





    private MessageDefinition messagedefinition;




    private List<Actions_ActionMessageExpression> actions_actionmessageexpressions;


    public HALL_Actions_MessageInvocation(
        boolean isTopDown    ) {
        super(
        );
        this.isTopDown = isTopDown;
        this.actions_actionmessageexpressions = new ArrayList<>();
    }

    public HALL_Actions_MessageInvocation(
        boolean isTopDown        ArrayList<Actions_ActionMessageExpression> actions_actionmessageexpressions    ) {
        this.isTopDown = isTopDown;
        this.actions_actionmessageexpressions = actions_actionmessageexpressions;
    }

    public boolean getIstopdown() {
        return isTopDown;
    }

    public void setIstopdown(boolean isTopDown) {
        this.isTopDown = isTopDown;
    }

    public MessageDefinition getMessagedefinition() {
        return messagedefinition;
    }

    public void setMessagedefinition(MessageDefinition messagedefinition) {
        this.messagedefinition = messagedefinition;
    }
    public List<Actions_ActionMessageExpression> getActions_actionmessageexpressions() {
        return actions_actionmessageexpressions;
    }

    public void addActions_actionmessageexpression(Actions_actionmessageexpression actions_actionmessageexpression) {
        this.actions_actionmessageexpressions.add(actions_actionmessageexpression);
    }

}