





import java.util.List;
import java.util.ArrayList;

public class driver_RetrieveFromSymbian  {

    private String group;





    private driver_Task driver_task;


    public driver_RetrieveFromSymbian(
        String group    ) {
        this.group = group;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public driver_Task getDriver_task() {
        return driver_task;
    }

    public void setDriver_task(driver_Task driver_task) {
        this.driver_task = driver_task;
    }

}