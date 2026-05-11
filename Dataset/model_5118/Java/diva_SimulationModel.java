





import java.util.List;
import java.util.ArrayList;

public class diva_SimulationModel extends DiVAModelElement {






    private List<diva_Scenario> diva_scenarios;


    public diva_SimulationModel(
    ) {
        super(
        );
        this.diva_scenarios = new ArrayList<>();
    }

    public diva_SimulationModel(
        ArrayList<diva_Scenario> diva_scenarios    ) {
        this.diva_scenarios = diva_scenarios;
    }


    public List<diva_Scenario> getDiva_scenarios() {
        return diva_scenarios;
    }

    public void addDiva_scenario(Diva_scenario diva_scenario) {
        this.diva_scenarios.add(diva_scenario);
    }

}