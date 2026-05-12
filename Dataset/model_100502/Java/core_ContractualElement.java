





import java.util.List;
import java.util.ArrayList;

public class core_ContractualElement extends IdentifiedElement {

    private String droppingReason;
    private String originDate;
    private String satisfactionLevel;
    private String sources;
    private String scheduleDate;
    private String timeCriticality;
    private boolean dropped;





    private List<core_EObject> core_eobjects;




    private List<core_EObject> core_eobjects;




    private List<core_EObject> core_eobjects;




    private core_ContractualElement core_contractualelement;




    private List<core_EObject> core_eobjects;


    public core_ContractualElement(
        String droppingReason,        String originDate,        String satisfactionLevel,        String sources,        String scheduleDate,        String timeCriticality,        boolean dropped    ) {
        super(
        );
        this.droppingReason = droppingReason;
        this.originDate = originDate;
        this.satisfactionLevel = satisfactionLevel;
        this.sources = sources;
        this.scheduleDate = scheduleDate;
        this.timeCriticality = timeCriticality;
        this.dropped = dropped;
        this.core_eobjects = new ArrayList<>();
        this.core_eobjects = new ArrayList<>();
        this.core_eobjects = new ArrayList<>();
        this.core_eobjects = new ArrayList<>();
    }

    public core_ContractualElement(
        String droppingReason,        String originDate,        String satisfactionLevel,        String sources,        String scheduleDate,        String timeCriticality,        boolean dropped        ArrayList<core_EObject> core_eobjects,        ArrayList<core_EObject> core_eobjects,        ArrayList<core_EObject> core_eobjects,        ArrayList<core_EObject> core_eobjects    ) {
        this.droppingReason = droppingReason;
        this.originDate = originDate;
        this.satisfactionLevel = satisfactionLevel;
        this.sources = sources;
        this.scheduleDate = scheduleDate;
        this.timeCriticality = timeCriticality;
        this.dropped = dropped;
        this.core_eobjects = core_eobjects;
        this.core_eobjects = core_eobjects;
        this.core_eobjects = core_eobjects;
        this.core_eobjects = core_eobjects;
    }

    public String getDroppingreason() {
        return droppingReason;
    }

    public void setDroppingreason(String droppingReason) {
        this.droppingReason = droppingReason;
    }
    public String getOrigindate() {
        return originDate;
    }

    public void setOrigindate(String originDate) {
        this.originDate = originDate;
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
    public boolean getDropped() {
        return dropped;
    }

    public void setDropped(boolean dropped) {
        this.dropped = dropped;
    }

    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }
    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }

}