





import java.util.List;
import java.util.ArrayList;

public class core_ContractualElement extends IdentifiedElement {

    private String scheduleDate;
    private String timeCriticality;
    private String droppingReason;
    private String satisfactionLevel;
    private String originDate;
    private String sources;
    private boolean dropped;





    private core_ContractualElement core_contractualelement;


    public core_ContractualElement(
        String scheduleDate,        String timeCriticality,        String droppingReason,        String satisfactionLevel,        String originDate,        String sources,        boolean dropped    ) {
        super(
        );
        this.scheduleDate = scheduleDate;
        this.timeCriticality = timeCriticality;
        this.droppingReason = droppingReason;
        this.satisfactionLevel = satisfactionLevel;
        this.originDate = originDate;
        this.sources = sources;
        this.dropped = dropped;
    }


    public String getScheduledate() {
        return scheduleDate;
    }

    public void setScheduledate(String scheduleDate) {
        this.scheduleDate = scheduleDate;
    }
    public String getTimecriticality() {
        return timeCriticality;
    }

    public void setTimecriticality(String timeCriticality) {
        this.timeCriticality = timeCriticality;
    }
    public String getDroppingreason() {
        return droppingReason;
    }

    public void setDroppingreason(String droppingReason) {
        this.droppingReason = droppingReason;
    }
    public String getSatisfactionlevel() {
        return satisfactionLevel;
    }

    public void setSatisfactionlevel(String satisfactionLevel) {
        this.satisfactionLevel = satisfactionLevel;
    }
    public String getOrigindate() {
        return originDate;
    }

    public void setOrigindate(String originDate) {
        this.originDate = originDate;
    }
    public String getSources() {
        return sources;
    }

    public void setSources(String sources) {
        this.sources = sources;
    }
    public boolean getDropped() {
        return dropped;
    }

    public void setDropped(boolean dropped) {
        this.dropped = dropped;
    }

    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}