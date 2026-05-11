





import java.util.List;
import java.util.ArrayList;

public class conversation_StateMachine  {






    private conversation_Agent conversation_agent;




    private List<conversation_State> conversation_states;




    private conversation_State conversation_state;




    private conversation_State conversation_state;




    private conversation_Agent conversation_agent;




    private conversation_Transition conversation_transition;


    public conversation_StateMachine(
    ) {
        this.conversation_states = new ArrayList<>();
    }

    public conversation_StateMachine(
        ArrayList<conversation_State> conversation_states    ) {
        this.conversation_states = conversation_states;
    }


    public conversation_Agent getConversation_agent() {
        return conversation_agent;
    }

    public void setConversation_agent(conversation_Agent conversation_agent) {
        this.conversation_agent = conversation_agent;
    }
    public List<conversation_State> getConversation_states() {
        return conversation_states;
    }

    public void addConversation_state(Conversation_state conversation_state) {
        this.conversation_states.add(conversation_state);
    }
    public conversation_State getConversation_state() {
        return conversation_state;
    }

    public void setConversation_state(conversation_State conversation_state) {
        this.conversation_state = conversation_state;
    }
    public conversation_State getConversation_state() {
        return conversation_state;
    }

    public void setConversation_state(conversation_State conversation_state) {
        this.conversation_state = conversation_state;
    }
    public conversation_Agent getConversation_agent() {
        return conversation_agent;
    }

    public void setConversation_agent(conversation_Agent conversation_agent) {
        this.conversation_agent = conversation_agent;
    }
    public conversation_Transition getConversation_transition() {
        return conversation_transition;
    }

    public void setConversation_transition(conversation_Transition conversation_transition) {
        this.conversation_transition = conversation_transition;
    }

}