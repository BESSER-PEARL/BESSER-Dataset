





import java.util.List;
import java.util.ArrayList;

public class WT_ControlSubsystem  {

    private String name;





    private WT_Subsystem wt_subsystem;


    public WT_ControlSubsystem(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public WT_Subsystem getWt_subsystem() {
        return wt_subsystem;
    }

    public void setWt_subsystem(WT_Subsystem wt_subsystem) {
        this.wt_subsystem = wt_subsystem;
    }

}