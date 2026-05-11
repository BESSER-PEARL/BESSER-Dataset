





import java.util.List;
import java.util.ArrayList;

public class thingml_ReceiveMessage extends Event {






    private thingml_Message thingml_message;




    private thingml_EventReference thingml_eventreference;




    private thingml_Port thingml_port;


    public thingml_ReceiveMessage(
    ) {
        super(
        );
    }



    public thingml_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingml_Message thingml_message) {
        this.thingml_message = thingml_message;
    }
    public thingml_EventReference getThingml_eventreference() {
        return thingml_eventreference;
    }

    public void setThingml_eventreference(thingml_EventReference thingml_eventreference) {
        this.thingml_eventreference = thingml_eventreference;
    }
    public thingml_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingml_Port thingml_port) {
        this.thingml_port = thingml_port;
    }

}