





import java.util.List;
import java.util.ArrayList;

public class driver_Dispatcher  {

    private None mmu;
    private None taskManager;
    private None cpus;





    private driver_Driver driver_driver;


    public driver_Dispatcher(
        None mmu,        None taskManager,        None cpus    ) {
        this.mmu = mmu;
        this.taskManager = taskManager;
        this.cpus = cpus;
    }


    public None getMmu() {
        return mmu;
    }

    public void setMmu(None mmu) {
        this.mmu = mmu;
    }
    public None getTaskmanager() {
        return taskManager;
    }

    public void setTaskmanager(None taskManager) {
        this.taskManager = taskManager;
    }
    public None getCpus() {
        return cpus;
    }

    public void setCpus(None cpus) {
        this.cpus = cpus;
    }

    public driver_Driver getDriver_driver() {
        return driver_driver;
    }

    public void setDriver_driver(driver_Driver driver_driver) {
        this.driver_driver = driver_driver;
    }

}