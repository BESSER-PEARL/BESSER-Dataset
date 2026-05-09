





import java.util.List;
import java.util.ArrayList;

public class simplepdl_SubWorkDefinition extends Activities {






    private List<simplepdl_ParameterSWD> simplepdl_parameterswds;




    private simplepdl_Activities simplepdl_activities;




    private simplepdl_ParameterSWD simplepdl_parameterswd;




    private simplepdl_Activities simplepdl_activities;


    public simplepdl_SubWorkDefinition(
    ) {
        super(
        );
        this.simplepdl_parameterswds = new ArrayList<>();
    }

    public simplepdl_SubWorkDefinition(
        ArrayList<simplepdl_ParameterSWD> simplepdl_parameterswds    ) {
        this.simplepdl_parameterswds = simplepdl_parameterswds;
    }


    public List<simplepdl_ParameterSWD> getSimplepdl_parameterswds() {
        return simplepdl_parameterswds;
    }

    public void addSimplepdl_parameterswd(Simplepdl_parameterswd simplepdl_parameterswd) {
        this.simplepdl_parameterswds.add(simplepdl_parameterswd);
    }
    public simplepdl_Activities getSimplepdl_activities() {
        return simplepdl_activities;
    }

    public void setSimplepdl_activities(simplepdl_Activities simplepdl_activities) {
        this.simplepdl_activities = simplepdl_activities;
    }
    public simplepdl_ParameterSWD getSimplepdl_parameterswd() {
        return simplepdl_parameterswd;
    }

    public void setSimplepdl_parameterswd(simplepdl_ParameterSWD simplepdl_parameterswd) {
        this.simplepdl_parameterswd = simplepdl_parameterswd;
    }
    public simplepdl_Activities getSimplepdl_activities() {
        return simplepdl_activities;
    }

    public void setSimplepdl_activities(simplepdl_Activities simplepdl_activities) {
        this.simplepdl_activities = simplepdl_activities;
    }

}