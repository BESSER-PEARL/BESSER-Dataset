





import java.util.List;
import java.util.ArrayList;

public class thingML_MessageParameter extends ReferencedElmt {

    private String name;





    private thingML_Message thingml_message;


    public thingML_MessageParameter(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public thingML_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingML_Message thingml_message) {
        this.thingml_message = thingml_message;
    }

}