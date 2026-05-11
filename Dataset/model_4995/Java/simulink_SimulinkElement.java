





import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkElement  {

    private String name;
    private String handle;



    public simulink_SimulinkElement(
        String name,        String handle    ) {
        this.name = name;
        this.handle = handle;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHandle() {
        return handle;
    }

    public void setHandle(String handle) {
        this.handle = handle;
    }


}