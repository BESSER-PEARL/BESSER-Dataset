





import java.util.List;
import java.util.ArrayList;

public class iotsystem_Parameter  {

    private String value;
    private String name;





    private iotsystem_Action iotsystem_action;


    public iotsystem_Parameter(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotsystem_Action getIotsystem_action() {
        return iotsystem_action;
    }

    public void setIotsystem_action(iotsystem_Action iotsystem_action) {
        this.iotsystem_action = iotsystem_action;
    }

}