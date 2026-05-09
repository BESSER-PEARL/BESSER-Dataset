





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_Enable extends ActionMessageExpression {






    private FSMActions_ActionExpression fsmactions_actionexpression;




    private MessageDefinition messagedefinition;


    public HALL_FSMActions_Enable(
    ) {
        super(
        );
    }



    public FSMActions_ActionExpression getFsmactions_actionexpression() {
        return fsmactions_actionexpression;
    }

    public void setFsmactions_actionexpression(FSMActions_ActionExpression fsmactions_actionexpression) {
        this.fsmactions_actionexpression = fsmactions_actionexpression;
    }
    public MessageDefinition getMessagedefinition() {
        return messagedefinition;
    }

    public void setMessagedefinition(MessageDefinition messagedefinition) {
        this.messagedefinition = messagedefinition;
    }

}