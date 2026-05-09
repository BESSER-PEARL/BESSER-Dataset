





import java.util.List;
import java.util.ArrayList;

public class model_requirement_NonFunctionalRequirement extends Criterion {






    private List<requirement_Scenario> requirement_scenarios;




    private List<requirement_UseCase> requirement_usecases;


    public model_requirement_NonFunctionalRequirement(
    ) {
        super(
        );
        this.requirement_scenarios = new ArrayList<>();
        this.requirement_usecases = new ArrayList<>();
    }

    public model_requirement_NonFunctionalRequirement(
        ArrayList<requirement_Scenario> requirement_scenarios,        ArrayList<requirement_UseCase> requirement_usecases    ) {
        this.requirement_scenarios = requirement_scenarios;
        this.requirement_usecases = requirement_usecases;
    }


    public List<requirement_Scenario> getRequirement_scenarios() {
        return requirement_scenarios;
    }

    public void addRequirement_scenario(Requirement_scenario requirement_scenario) {
        this.requirement_scenarios.add(requirement_scenario);
    }
    public List<requirement_UseCase> getRequirement_usecases() {
        return requirement_usecases;
    }

    public void addRequirement_usecase(Requirement_usecase requirement_usecase) {
        this.requirement_usecases.add(requirement_usecase);
    }

}