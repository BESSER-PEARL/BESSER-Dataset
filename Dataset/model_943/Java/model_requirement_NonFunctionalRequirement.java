





import java.util.List;
import java.util.ArrayList;

public class model_requirement_NonFunctionalRequirement extends Criterion {






    private List<requirement_UseCase> requirement_usecases;




    private List<requirement_SystemFunction> requirement_systemfunctions;




    private List<requirement_Scenario> requirement_scenarios;




    private List<requirement_UserTask> requirement_usertasks;


    public model_requirement_NonFunctionalRequirement(
    ) {
        super(
        );
        this.requirement_usecases = new ArrayList<>();
        this.requirement_systemfunctions = new ArrayList<>();
        this.requirement_scenarios = new ArrayList<>();
        this.requirement_usertasks = new ArrayList<>();
    }

    public model_requirement_NonFunctionalRequirement(
        ArrayList<requirement_UseCase> requirement_usecases,        ArrayList<requirement_SystemFunction> requirement_systemfunctions,        ArrayList<requirement_Scenario> requirement_scenarios,        ArrayList<requirement_UserTask> requirement_usertasks    ) {
        this.requirement_usecases = requirement_usecases;
        this.requirement_systemfunctions = requirement_systemfunctions;
        this.requirement_scenarios = requirement_scenarios;
        this.requirement_usertasks = requirement_usertasks;
    }


    public List<requirement_UseCase> getRequirement_usecases() {
        return requirement_usecases;
    }

    public void addRequirement_usecase(Requirement_usecase requirement_usecase) {
        this.requirement_usecases.add(requirement_usecase);
    }
    public List<requirement_SystemFunction> getRequirement_systemfunctions() {
        return requirement_systemfunctions;
    }

    public void addRequirement_systemfunction(Requirement_systemfunction requirement_systemfunction) {
        this.requirement_systemfunctions.add(requirement_systemfunction);
    }
    public List<requirement_Scenario> getRequirement_scenarios() {
        return requirement_scenarios;
    }

    public void addRequirement_scenario(Requirement_scenario requirement_scenario) {
        this.requirement_scenarios.add(requirement_scenario);
    }
    public List<requirement_UserTask> getRequirement_usertasks() {
        return requirement_usertasks;
    }

    public void addRequirement_usertask(Requirement_usertask requirement_usertask) {
        this.requirement_usertasks.add(requirement_usertask);
    }

}