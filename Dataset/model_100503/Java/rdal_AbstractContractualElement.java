





import java.util.List;
import java.util.ArrayList;

public class rdal_AbstractContractualElement extends TraceableToDesignElementsElement {

    private String scheduleDate;
    private String originDate;
    private String sources;
    private boolean dropped;





    private List<rdal_Rationale> rdal_rationales;




    private List<rdal_Stakeholder> rdal_stakeholders;




    private List<rdal_Rationale> rdal_rationales;




    private List<rdal_ContactInformation> rdal_contactinformations;




    private rdal_AbstractContractualElement rdal_abstractcontractualelement;




    private rdal_Uncertainty rdal_uncertainty;




    private rdal_Conflict rdal_conflict;


    public rdal_AbstractContractualElement(
        String scheduleDate,        String originDate,        String sources,        boolean dropped    ) {
        super(
        );
        this.scheduleDate = scheduleDate;
        this.originDate = originDate;
        this.sources = sources;
        this.dropped = dropped;
        this.rdal_rationales = new ArrayList<>();
        this.rdal_stakeholders = new ArrayList<>();
        this.rdal_rationales = new ArrayList<>();
        this.rdal_contactinformations = new ArrayList<>();
    }

    public rdal_AbstractContractualElement(
        String scheduleDate,        String originDate,        String sources,        boolean dropped        ArrayList<rdal_Rationale> rdal_rationales,        ArrayList<rdal_Stakeholder> rdal_stakeholders,        ArrayList<rdal_Rationale> rdal_rationales,        ArrayList<rdal_ContactInformation> rdal_contactinformations    ) {
        this.scheduleDate = scheduleDate;
        this.originDate = originDate;
        this.sources = sources;
        this.dropped = dropped;
        this.rdal_rationales = rdal_rationales;
        this.rdal_stakeholders = rdal_stakeholders;
        this.rdal_rationales = rdal_rationales;
        this.rdal_contactinformations = rdal_contactinformations;
    }

    public String getScheduledate() {
        return scheduleDate;
    }

    public void setScheduledate(String scheduleDate) {
        this.scheduleDate = scheduleDate;
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

    public List<rdal_Rationale> getRdal_rationales() {
        return rdal_rationales;
    }

    public void addRdal_rationale(Rdal_rationale rdal_rationale) {
        this.rdal_rationales.add(rdal_rationale);
    }
    public List<rdal_Stakeholder> getRdal_stakeholders() {
        return rdal_stakeholders;
    }

    public void addRdal_stakeholder(Rdal_stakeholder rdal_stakeholder) {
        this.rdal_stakeholders.add(rdal_stakeholder);
    }
    public List<rdal_Rationale> getRdal_rationales() {
        return rdal_rationales;
    }

    public void addRdal_rationale(Rdal_rationale rdal_rationale) {
        this.rdal_rationales.add(rdal_rationale);
    }
    public List<rdal_ContactInformation> getRdal_contactinformations() {
        return rdal_contactinformations;
    }

    public void addRdal_contactinformation(Rdal_contactinformation rdal_contactinformation) {
        this.rdal_contactinformations.add(rdal_contactinformation);
    }
    public rdal_AbstractContractualElement getRdal_abstractcontractualelement() {
        return rdal_abstractcontractualelement;
    }

    public void setRdal_abstractcontractualelement(rdal_AbstractContractualElement rdal_abstractcontractualelement) {
        this.rdal_abstractcontractualelement = rdal_abstractcontractualelement;
    }
    public rdal_Uncertainty getRdal_uncertainty() {
        return rdal_uncertainty;
    }

    public void setRdal_uncertainty(rdal_Uncertainty rdal_uncertainty) {
        this.rdal_uncertainty = rdal_uncertainty;
    }
    public rdal_Conflict getRdal_conflict() {
        return rdal_conflict;
    }

    public void setRdal_conflict(rdal_Conflict rdal_conflict) {
        this.rdal_conflict = rdal_conflict;
    }

}