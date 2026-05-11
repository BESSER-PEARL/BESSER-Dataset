





import java.util.List;
import java.util.ArrayList;

public class WT_StateMachine  {

    private String name;





    private WT_ControlSubsystem wt_controlsubsystem;




    private WT_Component wt_component;


    public WT_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public WT_ControlSubsystem getWt_controlsubsystem() {
        return wt_controlsubsystem;
    }

    public void setWt_controlsubsystem(WT_ControlSubsystem wt_controlsubsystem) {
        this.wt_controlsubsystem = wt_controlsubsystem;
    }
    public WT_Component getWt_component() {
        return wt_component;
    }

    public void setWt_component(WT_Component wt_component) {
        this.wt_component = wt_component;
    }

}