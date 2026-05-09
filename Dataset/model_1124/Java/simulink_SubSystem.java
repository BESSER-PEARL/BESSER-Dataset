





import java.util.List;
import java.util.ArrayList;

public class simulink_SubSystem extends Block {






    private List<simulink_SubSystem> simulink_subsystems;


    public simulink_SubSystem(
    ) {
        super(
        );
        this.simulink_subsystems = new ArrayList<>();
    }

    public simulink_SubSystem(
        ArrayList<simulink_SubSystem> simulink_subsystems    ) {
        this.simulink_subsystems = simulink_subsystems;
    }


    public List<simulink_SubSystem> getSimulink_subsystems() {
        return simulink_subsystems;
    }

    public void addSimulink_subsystem(Simulink_subsystem simulink_subsystem) {
        this.simulink_subsystems.add(simulink_subsystem);
    }

}