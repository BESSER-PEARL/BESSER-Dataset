





import java.util.List;
import java.util.ArrayList;

public class driver_ExecuteOnSymbian  {

    private String group;





    private driver_Task driver_task;




    private List<driver_Rtest> driver_rtests;




    private List<driver_CmdSymbian> driver_cmdsymbians;


    public driver_ExecuteOnSymbian(
        String group    ) {
        this.group = group;
        this.driver_rtests = new ArrayList<>();
        this.driver_cmdsymbians = new ArrayList<>();
    }

    public driver_ExecuteOnSymbian(
        String group        ArrayList<driver_Rtest> driver_rtests,        ArrayList<driver_CmdSymbian> driver_cmdsymbians    ) {
        this.group = group;
        this.driver_rtests = driver_rtests;
        this.driver_cmdsymbians = driver_cmdsymbians;
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
    public List<driver_Rtest> getDriver_rtests() {
        return driver_rtests;
    }

    public void addDriver_rtest(Driver_rtest driver_rtest) {
        this.driver_rtests.add(driver_rtest);
    }
    public List<driver_CmdSymbian> getDriver_cmdsymbians() {
        return driver_cmdsymbians;
    }

    public void addDriver_cmdsymbian(Driver_cmdsymbian driver_cmdsymbian) {
        this.driver_cmdsymbians.add(driver_cmdsymbian);
    }

}