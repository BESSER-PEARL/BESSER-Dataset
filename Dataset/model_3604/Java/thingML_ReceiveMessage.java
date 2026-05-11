





import java.util.List;
import java.util.ArrayList;

public class thingML_ReceiveMessage extends Event {






    private thingML_Message thingml_message;




    private thingML_Port thingml_port;


    public thingML_ReceiveMessage(
    ) {
        super(
        );
    }



    public thingML_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingML_Message thingml_message) {
        this.thingml_message = thingml_message;
    }
    public thingML_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingML_Port thingml_port) {
        this.thingml_port = thingml_port;
    }

}