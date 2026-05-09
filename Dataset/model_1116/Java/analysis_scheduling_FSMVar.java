





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSMVar  {

    private String type;
    private String name;
    private String initialVal;



    public analysis_scheduling_FSMVar(
        String type,        String name,        String initialVal    ) {
        this.type = type;
        this.name = name;
        this.initialVal = initialVal;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInitialval() {
        return initialVal;
    }

    public void setInitialval(String initialVal) {
        this.initialVal = initialVal;
    }


}