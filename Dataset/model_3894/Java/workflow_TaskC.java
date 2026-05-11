





import java.util.List;
import java.util.ArrayList;

public class workflow_TaskC extends TaskAspect {

    private String name;



    public workflow_TaskC(
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


}