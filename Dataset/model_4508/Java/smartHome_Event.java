





import java.util.List;
import java.util.ArrayList;

public class smartHome_Event  {

    private String description;





    private smartHome_Rule smarthome_rule;


    public smartHome_Event(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public smartHome_Rule getSmarthome_rule() {
        return smarthome_rule;
    }

    public void setSmarthome_rule(smartHome_Rule smarthome_rule) {
        this.smarthome_rule = smarthome_rule;
    }

}