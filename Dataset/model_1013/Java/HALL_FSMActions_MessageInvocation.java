





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_MessageInvocation extends ActionExpression {

    private boolean isTopDown;





    private List<FSMActions_ActionExpression> fsmactions_actionexpressions;




    private MessageDefinition messagedefinition;


    public HALL_FSMActions_MessageInvocation(
        boolean isTopDown    ) {
        super(
        );
        this.isTopDown = isTopDown;
        this.fsmactions_actionexpressions = new ArrayList<>();
    }

    public HALL_FSMActions_MessageInvocation(
        boolean isTopDown        ArrayList<FSMActions_ActionExpression> fsmactions_actionexpressions    ) {
        this.isTopDown = isTopDown;
        this.fsmactions_actionexpressions = fsmactions_actionexpressions;
    }

    public boolean getIstopdown() {
        return isTopDown;
    }

    public void setIstopdown(boolean isTopDown) {
        this.isTopDown = isTopDown;
    }

    public List<FSMActions_ActionExpression> getFsmactions_actionexpressions() {
        return fsmactions_actionexpressions;
    }

    public void addFsmactions_actionexpression(Fsmactions_actionexpression fsmactions_actionexpression) {
        this.fsmactions_actionexpressions.add(fsmactions_actionexpression);
    }
    public MessageDefinition getMessagedefinition() {
        return messagedefinition;
    }

    public void setMessagedefinition(MessageDefinition messagedefinition) {
        this.messagedefinition = messagedefinition;
    }

}