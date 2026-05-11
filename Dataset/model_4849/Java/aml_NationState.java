





import java.util.List;
import java.util.ArrayList;

public class aml_NationState  {

    private String group;
    private String actor;
    private String event;
    private String region;
    private String perspective;



    public aml_NationState(
        String group,        String actor,        String event,        String region,        String perspective    ) {
        this.group = group;
        this.actor = actor;
        this.event = event;
        this.region = region;
        this.perspective = perspective;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public String getPerspective() {
        return perspective;
    }

    public void setPerspective(String perspective) {
        this.perspective = perspective;
    }


}