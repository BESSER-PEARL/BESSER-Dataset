





import java.util.List;
import java.util.ArrayList;

public class WT_Subsystem  {

    private String name;





    private WT_WTComponents wt_wtcomponents;




    private WT_Subsystem wt_subsystem;


    public WT_Subsystem(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public WT_WTComponents getWt_wtcomponents() {
        return wt_wtcomponents;
    }

    public void setWt_wtcomponents(WT_WTComponents wt_wtcomponents) {
        this.wt_wtcomponents = wt_wtcomponents;
    }
    public WT_Subsystem getWt_subsystem() {
        return wt_subsystem;
    }

    public void setWt_subsystem(WT_Subsystem wt_subsystem) {
        this.wt_subsystem = wt_subsystem;
    }

}