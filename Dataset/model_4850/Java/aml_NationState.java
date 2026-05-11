





import java.util.List;
import java.util.ArrayList;

public class aml_NationState  {

    private String actor;
    private String event;
    private String region;
    private String group;
    private String perspective;





    private aml_Coverage aml_coverage;


    public aml_NationState(
        String actor,        String event,        String region,        String group,        String perspective    ) {
        this.actor = actor;
        this.event = event;
        this.region = region;
        this.group = group;
        this.perspective = perspective;
    }


    public String getActor() {
        return actor;
    }

    public void setActor(String actor) {
        this.actor = actor;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
        this.region = region;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getPerspective() {
        return perspective;
    }

    public void setPerspective(String perspective) {
        this.perspective = perspective;
    }

    public aml_Coverage getAml_coverage() {
        return aml_coverage;
    }

    public void setAml_coverage(aml_Coverage aml_coverage) {
        this.aml_coverage = aml_coverage;
    }

}