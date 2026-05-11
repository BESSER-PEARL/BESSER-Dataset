





import java.util.List;
import java.util.ArrayList;

public class arduino_Task  {

    private boolean external;
    private String name;



    public arduino_Task(
        boolean external,        String name    ) {
        this.external = external;
        this.name = name;
    }


    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}