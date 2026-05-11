





import java.util.List;
import java.util.ArrayList;

public class conversation_Event  {

    private String name;





    private conversation_Projection conversation_projection;


    public conversation_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public conversation_Projection getConversation_projection() {
        return conversation_projection;
    }

    public void setConversation_projection(conversation_Projection conversation_projection) {
        this.conversation_projection = conversation_projection;
    }

}