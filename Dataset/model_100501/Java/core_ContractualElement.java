





import java.util.List;
import java.util.ArrayList;

public class core_ContractualElement extends IdentifiedElement {

    private boolean dropped;
    private String originDate;
    private String timeCriticality;
    private String satisfactionLevel;
    private String sources;
    private String droppingReason;
    private String scheduleDate;





    private List<core_ContractualElement> core_contractualelements;


    public core_ContractualElement(
        boolean dropped,        String originDate,        String timeCriticality,        String satisfactionLevel,        String sources,        String droppingReason,        String scheduleDate    ) {
        super(
        );
        this.dropped = dropped;
        this.originDate = originDate;
        this.timeCriticality = timeCriticality;
        this.satisfactionLevel = satisfactionLevel;
        this.sources = sources;
        this.droppingReason = droppingReason;
        this.scheduleDate = scheduleDate;
        this.core_contractualelements = new ArrayList<>();
    }

    public core_ContractualElement(
        boolean dropped,        String originDate,        String timeCriticality,        String satisfactionLevel,        String sources,        String droppingReason,        String scheduleDate        ArrayList<core_ContractualElement> core_contractualelements    ) {
        this.dropped = dropped;
        this.originDate = originDate;
        this.timeCriticality = timeCriticality;
        this.satisfactionLevel = satisfactionLevel;
        this.sources = sources;
        this.droppingReason = droppingReason;
        this.scheduleDate = scheduleDate;
        this.core_contractualelements = core_contractualelements;
    }

    public boolean getDropped() {
        return dropped;
    }

    public void setDropped(boolean dropped) {
        this.dropped = dropped;
    }
    public String getOrigindate() {
        return originDate;
    }

    public void setOrigindate(String originDate) {
        this.originDate = originDate;
    }
    public String getTimecriticality() {
        return timeCriticality;
    }

    public void setTimecriticality(String timeCriticality) {
        this.timeCriticality = timeCriticality;
    }
    public String getSatisfactionlevel() {
        return satisfactionLevel;
    }

    public void setSatisfactionlevel(String satisfactionLevel) {
        this.satisfactionLevel = satisfactionLevel;
    }
    public String getSources() {
        return sources;
    }

    public void setSources(String sources) {
        this.sources = sources;
    }
    public String getDroppingreason() {
        return droppingReason;
    }

    public void setDroppingreason(String droppingReason) {
        this.droppingReason = droppingReason;
    }
    public String getScheduledate() {
        return scheduleDate;
    }

    public void setScheduledate(String scheduleDate) {
        this.scheduleDate = scheduleDate;
    }

    public List<core_ContractualElement> getCore_contractualelements() {
        return core_contractualelements;
    }

    public void addCore_contractualelement(Core_contractualelement core_contractualelement) {
        this.core_contractualelements.add(core_contractualelement);
    }

}