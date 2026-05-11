





import java.util.List;
import java.util.ArrayList;

public class drone_Parameter  {

    private String key;
    private String description;





    private drone_Action drone_action;


    public drone_Parameter(
        String key,        String description    ) {
        this.key = key;
        this.description = description;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public drone_Action getDrone_action() {
        return drone_action;
    }

    public void setDrone_action(drone_Action drone_action) {
        this.drone_action = drone_action;
    }

}