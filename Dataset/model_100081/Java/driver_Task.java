





import java.util.List;
import java.util.ArrayList;

public class driver_Task  {

    private String group;
    private String name;
    private String preRebootDevice;
    private String timeout;





    private driver_Driver driver_driver;




    private List<driver_Task> driver_tasks;


    public driver_Task(
        String group,        String name,        String preRebootDevice,        String timeout    ) {
        this.group = group;
        this.name = name;
        this.preRebootDevice = preRebootDevice;
        this.timeout = timeout;
        this.driver_tasks = new ArrayList<>();
    }

    public driver_Task(
        String group,        String name,        String preRebootDevice,        String timeout        ArrayList<driver_Task> driver_tasks    ) {
        this.group = group;
        this.name = name;
        this.preRebootDevice = preRebootDevice;
        this.timeout = timeout;
        this.driver_tasks = driver_tasks;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrerebootdevice() {
        return preRebootDevice;
    }

    public void setPrerebootdevice(String preRebootDevice) {
        this.preRebootDevice = preRebootDevice;
    }
    public String getTimeout() {
        return timeout;
    }

    public void setTimeout(String timeout) {
        this.timeout = timeout;
    }

    public driver_Driver getDriver_driver() {
        return driver_driver;
    }

    public void setDriver_driver(driver_Driver driver_driver) {
        this.driver_driver = driver_driver;
    }
    public List<driver_Task> getDriver_tasks() {
        return driver_tasks;
    }

    public void addDriver_task(Driver_task driver_task) {
        this.driver_tasks.add(driver_task);
    }

}