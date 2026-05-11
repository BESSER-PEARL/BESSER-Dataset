





import java.util.List;
import java.util.ArrayList;

public class conversation_AgentImport extends Import {






    private conversation_Agent conversation_agent;




    private conversation_Conversation conversation_conversation;


    public conversation_AgentImport(
    ) {
        super(
        );
    }



    public conversation_Agent getConversation_agent() {
        return conversation_agent;
    }

    public void setConversation_agent(conversation_Agent conversation_agent) {
        this.conversation_agent = conversation_agent;
    }
    public conversation_Conversation getConversation_conversation() {
        return conversation_conversation;
    }

    public void setConversation_conversation(conversation_Conversation conversation_conversation) {
        this.conversation_conversation = conversation_conversation;
    }

}