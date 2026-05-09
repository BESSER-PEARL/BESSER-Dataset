





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_PosConditionMessageExpression  {






    private MessageTransition messagetransition;




    private List<Instructions_PosConditionMessageExpressionElement> instructions_posconditionmessageexpressionelements;


    public HALL_Instructions_PosConditionMessageExpression(
    ) {
        this.instructions_posconditionmessageexpressionelements = new ArrayList<>();
    }

    public HALL_Instructions_PosConditionMessageExpression(
        ArrayList<Instructions_PosConditionMessageExpressionElement> instructions_posconditionmessageexpressionelements    ) {
        this.instructions_posconditionmessageexpressionelements = instructions_posconditionmessageexpressionelements;
    }


    public MessageTransition getMessagetransition() {
        return messagetransition;
    }

    public void setMessagetransition(MessageTransition messagetransition) {
        this.messagetransition = messagetransition;
    }
    public List<Instructions_PosConditionMessageExpressionElement> getInstructions_posconditionmessageexpressionelements() {
        return instructions_posconditionmessageexpressionelements;
    }

    public void addInstructions_posconditionmessageexpressionelement(Instructions_posconditionmessageexpressionelement instructions_posconditionmessageexpressionelement) {
        this.instructions_posconditionmessageexpressionelements.add(instructions_posconditionmessageexpressionelement);
    }

}