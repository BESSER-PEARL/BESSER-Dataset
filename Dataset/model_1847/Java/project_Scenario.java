





import java.util.List;
import java.util.ArrayList;

public class project_Scenario extends ProjectAttribute {

    private String name;
    private String id;
    private String active;





    private project_Scenario project_scenario;




    private project_ScenarioIcal project_scenarioical;




    private project_Scenarios project_scenarios;


    public project_Scenario(
        String name,        String id,        String active    ) {
        super(
        );
        this.name = name;
        this.id = id;
        this.active = active;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }

    public project_Scenario getProject_scenario() {
        return project_scenario;
    }

    public void setProject_scenario(project_Scenario project_scenario) {
        this.project_scenario = project_scenario;
    }
    public project_ScenarioIcal getProject_scenarioical() {
        return project_scenarioical;
    }

    public void setProject_scenarioical(project_ScenarioIcal project_scenarioical) {
        this.project_scenarioical = project_scenarioical;
    }
    public project_Scenarios getProject_scenarios() {
        return project_scenarios;
    }

    public void setProject_scenarios(project_Scenarios project_scenarios) {
        this.project_scenarios = project_scenarios;
    }

}