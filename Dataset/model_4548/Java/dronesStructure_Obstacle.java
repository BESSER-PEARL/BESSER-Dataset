





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_Obstacle extends AABB, NamedElement {






    private dronesStructure_Scenario dronesstructure_scenario;


    public dronesStructure_Obstacle(
    ) {
        super(
        );
    }



    public dronesStructure_Scenario getDronesstructure_scenario() {
        return dronesstructure_scenario;
    }

    public void setDronesstructure_scenario(dronesStructure_Scenario dronesstructure_scenario) {
        this.dronesstructure_scenario = dronesstructure_scenario;
    }

}