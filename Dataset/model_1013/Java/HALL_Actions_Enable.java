





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_Enable extends ActionMessageExpression {






    private List<Actions_ActionMessageExpression> actions_actionmessageexpressions;




    private MessageDefinition messagedefinition;


    public HALL_Actions_Enable(
    ) {
        super(
        );
        this.actions_actionmessageexpressions = new ArrayList<>();
    }

    public HALL_Actions_Enable(
        ArrayList<Actions_ActionMessageExpression> actions_actionmessageexpressions    ) {
        this.actions_actionmessageexpressions = actions_actionmessageexpressions;
    }


    public List<Actions_ActionMessageExpression> getActions_actionmessageexpressions() {
        return actions_actionmessageexpressions;
    }

    public void addActions_actionmessageexpression(Actions_actionmessageexpression actions_actionmessageexpression) {
        this.actions_actionmessageexpressions.add(actions_actionmessageexpression);
    }
    public MessageDefinition getMessagedefinition() {
        return messagedefinition;
    }

    public void setMessagedefinition(MessageDefinition messagedefinition) {
        this.messagedefinition = messagedefinition;
    }

}