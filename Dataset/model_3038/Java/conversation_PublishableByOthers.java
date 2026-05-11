





import java.util.List;
import java.util.ArrayList;

public class conversation_PublishableByOthers extends Event {






    private conversation_Transition conversation_transition;


    public conversation_PublishableByOthers(
    ) {
        super(
        );
    }



    public conversation_Transition getConversation_transition() {
        return conversation_transition;
    }

    public void setConversation_transition(conversation_Transition conversation_transition) {
        this.conversation_transition = conversation_transition;
    }

}