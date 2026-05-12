





import java.util.List;
import java.util.ArrayList;

public class driver_Scheduler  {

    private None taskManager;
    private None disk;
    private None schedulingMethod;
    private None mmu;





    private driver_Driver driver_driver;


    public driver_Scheduler(
        None taskManager,        None disk,        None schedulingMethod,        None mmu    ) {
        this.taskManager = taskManager;
        this.disk = disk;
        this.schedulingMethod = schedulingMethod;
        this.mmu = mmu;
    }


    public None getTaskmanager() {
        return taskManager;
    }

    public void setTaskmanager(None taskManager) {
        this.taskManager = taskManager;
    }
    public None getDisk() {
        return disk;
    }

    public void setDisk(None disk) {
        this.disk = disk;
    }
    public None getSchedulingmethod() {
        return schedulingMethod;
    }

    public void setSchedulingmethod(None schedulingMethod) {
        this.schedulingMethod = schedulingMethod;
    }
    public None getMmu() {
        return mmu;
    }

    public void setMmu(None mmu) {
        this.mmu = mmu;
    }

    public driver_Driver getDriver_driver() {
        return driver_driver;
    }

    public void setDriver_driver(driver_Driver driver_driver) {
        this.driver_driver = driver_driver;
    }

}