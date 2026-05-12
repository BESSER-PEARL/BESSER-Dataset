





import java.util.List;
import java.util.ArrayList;

public class driver_ExecuteOnPC  {

    private String group;





    private List<driver_Build> driver_builds;




    private driver_Task driver_task;




    private List<driver_CmdPC> driver_cmdpcs;


    public driver_ExecuteOnPC(
        String group    ) {
        this.group = group;
        this.driver_builds = new ArrayList<>();
        this.driver_cmdpcs = new ArrayList<>();
    }

    public driver_ExecuteOnPC(
        String group        ArrayList<driver_Build> driver_builds,        ArrayList<driver_CmdPC> driver_cmdpcs    ) {
        this.group = group;
        this.driver_builds = driver_builds;
        this.driver_cmdpcs = driver_cmdpcs;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<driver_Build> getDriver_builds() {
        return driver_builds;
    }

    public void addDriver_build(Driver_build driver_build) {
        this.driver_builds.add(driver_build);
    }
    public driver_Task getDriver_task() {
        return driver_task;
    }

    public void setDriver_task(driver_Task driver_task) {
        this.driver_task = driver_task;
    }
    public List<driver_CmdPC> getDriver_cmdpcs() {
        return driver_cmdpcs;
    }

    public void addDriver_cmdpc(Driver_cmdpc driver_cmdpc) {
        this.driver_cmdpcs.add(driver_cmdpc);
    }

}