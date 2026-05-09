





import java.util.List;
import java.util.ArrayList;

public class HALL_Parameter  {

    private String name;
    private String type;





    private MessageDefinition messagedefinition;


    public HALL_Parameter(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public MessageDefinition getMessagedefinition() {
        return messagedefinition;
    }

    public void setMessagedefinition(MessageDefinition messagedefinition) {
        this.messagedefinition = messagedefinition;
    }

}