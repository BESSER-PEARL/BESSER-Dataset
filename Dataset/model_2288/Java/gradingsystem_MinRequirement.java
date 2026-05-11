





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_MinRequirement  {

    private int value;
    private String type;





    private gradingsystem_Task gradingsystem_task;


    public gradingsystem_MinRequirement(
        int value,        String type    ) {
        this.value = value;
        this.type = type;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public gradingsystem_Task getGradingsystem_task() {
        return gradingsystem_task;
    }

    public void setGradingsystem_task(gradingsystem_Task gradingsystem_task) {
        this.gradingsystem_task = gradingsystem_task;
    }

}