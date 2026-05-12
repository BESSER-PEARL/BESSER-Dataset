





import java.util.List;
import java.util.ArrayList;

public class driver_FlashROM  {

    private String pCPath;





    private driver_Task driver_task;


    public driver_FlashROM(
        String pCPath    ) {
        this.pCPath = pCPath;
    }


    public String getPcpath() {
        return pCPath;
    }

    public void setPcpath(String pCPath) {
        this.pCPath = pCPath;
    }

    public driver_Task getDriver_task() {
        return driver_task;
    }

    public void setDriver_task(driver_Task driver_task) {
        this.driver_task = driver_task;
    }

}