





import java.util.List;
import java.util.ArrayList;

public class eTJ_Scenario extends ProjectAttribute {

    private String active;
    private String name;
    private String id;





    private eTJ_Criterion etj_criterion;




    private eTJ_LogicalFlagExpression etj_logicalflagexpression;




    private eTJ_Scenarios etj_scenarios;




    private eTJ_TrackingScenario etj_trackingscenario;




    private eTJ_ScenarioIcal etj_scenarioical;




    private eTJ_Scenario etj_scenario;




    private eTJ_TaskAttribute etj_taskattribute;


    public eTJ_Scenario(
        String active,        String name,        String id    ) {
        super(
        );
        this.active = active;
        this.name = name;
        this.id = id;
    }


    public String getActive() {
        return active;
    }

    public void setActive(String active) {
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

    public eTJ_Criterion getEtj_criterion() {
        return etj_criterion;
    }

    public void setEtj_criterion(eTJ_Criterion etj_criterion) {
        this.etj_criterion = etj_criterion;
    }
    public eTJ_LogicalFlagExpression getEtj_logicalflagexpression() {
        return etj_logicalflagexpression;
    }

    public void setEtj_logicalflagexpression(eTJ_LogicalFlagExpression etj_logicalflagexpression) {
        this.etj_logicalflagexpression = etj_logicalflagexpression;
    }
    public eTJ_Scenarios getEtj_scenarios() {
        return etj_scenarios;
    }

    public void setEtj_scenarios(eTJ_Scenarios etj_scenarios) {
        this.etj_scenarios = etj_scenarios;
    }
    public eTJ_TrackingScenario getEtj_trackingscenario() {
        return etj_trackingscenario;
    }

    public void setEtj_trackingscenario(eTJ_TrackingScenario etj_trackingscenario) {
        this.etj_trackingscenario = etj_trackingscenario;
    }
    public eTJ_ScenarioIcal getEtj_scenarioical() {
        return etj_scenarioical;
    }

    public void setEtj_scenarioical(eTJ_ScenarioIcal etj_scenarioical) {
        this.etj_scenarioical = etj_scenarioical;
    }
    public eTJ_Scenario getEtj_scenario() {
        return etj_scenario;
    }

    public void setEtj_scenario(eTJ_Scenario etj_scenario) {
        this.etj_scenario = etj_scenario;
    }
    public eTJ_TaskAttribute getEtj_taskattribute() {
        return etj_taskattribute;
    }

    public void setEtj_taskattribute(eTJ_TaskAttribute etj_taskattribute) {
        this.etj_taskattribute = etj_taskattribute;
    }

}