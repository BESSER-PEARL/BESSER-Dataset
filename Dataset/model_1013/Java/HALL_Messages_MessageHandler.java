





import java.util.List;
import java.util.ArrayList;

public class HALL_Messages_MessageHandler  {






    private InitialMessageState initialmessagestate;




    private Messages_HALL_Component messages_hall_component;




    private MessageDefinition messagedefinition;


    public HALL_Messages_MessageHandler(
    ) {
    }



    public InitialMessageState getInitialmessagestate() {
        return initialmessagestate;
    }

    public void setInitialmessagestate(InitialMessageState initialmessagestate) {
        this.initialmessagestate = initialmessagestate;
    }
    public Messages_HALL_Component getMessages_hall_component() {
        return messages_hall_component;
    }

    public void setMessages_hall_component(Messages_HALL_Component messages_hall_component) {
        this.messages_hall_component = messages_hall_component;
    }
    public MessageDefinition getMessagedefinition() {
        return messagedefinition;
    }

    public void setMessagedefinition(MessageDefinition messagedefinition) {
        this.messagedefinition = messagedefinition;
    }

}