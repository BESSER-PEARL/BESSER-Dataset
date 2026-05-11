





import java.util.List;
import java.util.ArrayList;

public class conversation_Agent  {

    private String stateMachineType;
    private String name;
    private String connectionType;
    private String accessRequirement;





    private conversation_Conversation conversation_conversation;




    private conversation_Conversation conversation_conversation;


    public conversation_Agent(
        String stateMachineType,        String name,        String connectionType,        String accessRequirement    ) {
        this.stateMachineType = stateMachineType;
        this.name = name;
        this.connectionType = connectionType;
        this.accessRequirement = accessRequirement;
    }


    public String getStatemachinetype() {
        return stateMachineType;
    }

    public void setStatemachinetype(String stateMachineType) {
        this.stateMachineType = stateMachineType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConnectiontype() {
        return connectionType;
    }

    public void setConnectiontype(String connectionType) {
        this.connectionType = connectionType;
    }
    public String getAccessrequirement() {
        return accessRequirement;
    }

    public void setAccessrequirement(String accessRequirement) {
        this.accessRequirement = accessRequirement;
    }

    public conversation_Conversation getConversation_conversation() {
        return conversation_conversation;
    }

    public void setConversation_conversation(conversation_Conversation conversation_conversation) {
        this.conversation_conversation = conversation_conversation;
    }
    public conversation_Conversation getConversation_conversation() {
        return conversation_conversation;
    }

    public void setConversation_conversation(conversation_Conversation conversation_conversation) {
        this.conversation_conversation = conversation_conversation;
    }

}