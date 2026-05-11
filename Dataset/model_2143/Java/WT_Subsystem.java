





import java.util.List;
import java.util.ArrayList;

public class WT_Subsystem  {

    private String name;





    private WT_Subsystem wt_subsystem;




    private WT_WTComponents wt_wtcomponents;




    private List<WT_ControlSubsystem> wt_controlsubsystems;




    private List<WT_Architecture> wt_architectures;


    public WT_Subsystem(
        String name    ) {
        this.name = name;
        this.wt_controlsubsystems = new ArrayList<>();
        this.wt_architectures = new ArrayList<>();
    }

    public WT_Subsystem(
        String name        ArrayList<WT_ControlSubsystem> wt_controlsubsystems,        ArrayList<WT_Architecture> wt_architectures    ) {
        this.name = name;
        this.wt_controlsubsystems = wt_controlsubsystems;
        this.wt_architectures = wt_architectures;
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
    public WT_WTComponents getWt_wtcomponents() {
        return wt_wtcomponents;
    }

    public void setWt_wtcomponents(WT_WTComponents wt_wtcomponents) {
        this.wt_wtcomponents = wt_wtcomponents;
    }
    public List<WT_ControlSubsystem> getWt_controlsubsystems() {
        return wt_controlsubsystems;
    }

    public void addWt_controlsubsystem(Wt_controlsubsystem wt_controlsubsystem) {
        this.wt_controlsubsystems.add(wt_controlsubsystem);
    }
    public List<WT_Architecture> getWt_architectures() {
        return wt_architectures;
    }

    public void addWt_architecture(Wt_architecture wt_architecture) {
        this.wt_architectures.add(wt_architecture);
    }

}