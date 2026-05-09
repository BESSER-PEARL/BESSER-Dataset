





import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkFile extends SubSystem {






    private List<simulink_Bus> simulink_buss;


    public simulink_SimulinkFile(
    ) {
        super(
        );
        this.simulink_buss = new ArrayList<>();
    }

    public simulink_SimulinkFile(
        ArrayList<simulink_Bus> simulink_buss    ) {
        this.simulink_buss = simulink_buss;
    }


    public List<simulink_Bus> getSimulink_buss() {
        return simulink_buss;
    }

    public void addSimulink_bus(Simulink_bus simulink_bus) {
        this.simulink_buss.add(simulink_bus);
    }

}