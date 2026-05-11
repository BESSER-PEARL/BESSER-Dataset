





import java.util.List;
import java.util.ArrayList;

public class WT_Subsystem  {

    private String name;





    private List<WT_Subsystem> wt_subsystems;




    private WT_WTComponents wt_wtcomponents;


    public WT_Subsystem(
        String name    ) {
        this.name = name;
        this.wt_subsystems = new ArrayList<>();
    }

    public WT_Subsystem(
        String name        ArrayList<WT_Subsystem> wt_subsystems    ) {
        this.name = name;
        this.wt_subsystems = wt_subsystems;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<WT_Subsystem> getWt_subsystems() {
        return wt_subsystems;
    }

    public void addWt_subsystem(Wt_subsystem wt_subsystem) {
        this.wt_subsystems.add(wt_subsystem);
    }
    public WT_WTComponents getWt_wtcomponents() {
        return wt_wtcomponents;
    }

    public void setWt_wtcomponents(WT_WTComponents wt_wtcomponents) {
        this.wt_wtcomponents = wt_wtcomponents;
    }

}