





import java.util.List;
import java.util.ArrayList;

public class rdal_Specification extends SatisfiableElement, AbstractContractualElement, VerifiableElement {

    private String version;





    private rdal_RdalOrgPackage rdal_rdalorgpackage;




    private List<rdal_Stakeholder> rdal_stakeholders;




    private rdal_TraceableToDesignElementsElement rdal_traceabletodesignelementselement;




    private List<rdal_ActorReference> rdal_actorreferences;




    private List<rdal_Conflict> rdal_conflicts;




    private List<rdal_RdalOrgPackage> rdal_rdalorgpackages;




    private List<rdal_NonFunctionalProperty> rdal_nonfunctionalpropertys;




    private List<rdal_ContactInformation> rdal_contactinformations;


    public rdal_Specification(
        String version    ) {
        super(
        );
        this.version = version;
        this.rdal_stakeholders = new ArrayList<>();
        this.rdal_actorreferences = new ArrayList<>();
        this.rdal_conflicts = new ArrayList<>();
        this.rdal_rdalorgpackages = new ArrayList<>();
        this.rdal_nonfunctionalpropertys = new ArrayList<>();
        this.rdal_contactinformations = new ArrayList<>();
    }

    public rdal_Specification(
        String version        ArrayList<rdal_Stakeholder> rdal_stakeholders,        ArrayList<rdal_ActorReference> rdal_actorreferences,        ArrayList<rdal_Conflict> rdal_conflicts,        ArrayList<rdal_RdalOrgPackage> rdal_rdalorgpackages,        ArrayList<rdal_NonFunctionalProperty> rdal_nonfunctionalpropertys,        ArrayList<rdal_ContactInformation> rdal_contactinformations    ) {
        this.version = version;
        this.rdal_stakeholders = rdal_stakeholders;
        this.rdal_actorreferences = rdal_actorreferences;
        this.rdal_conflicts = rdal_conflicts;
        this.rdal_rdalorgpackages = rdal_rdalorgpackages;
        this.rdal_nonfunctionalpropertys = rdal_nonfunctionalpropertys;
        this.rdal_contactinformations = rdal_contactinformations;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public rdal_RdalOrgPackage getRdal_rdalorgpackage() {
        return rdal_rdalorgpackage;
    }

    public void setRdal_rdalorgpackage(rdal_RdalOrgPackage rdal_rdalorgpackage) {
        this.rdal_rdalorgpackage = rdal_rdalorgpackage;
    }
    public List<rdal_Stakeholder> getRdal_stakeholders() {
        return rdal_stakeholders;
    }

    public void addRdal_stakeholder(Rdal_stakeholder rdal_stakeholder) {
        this.rdal_stakeholders.add(rdal_stakeholder);
    }
    public rdal_TraceableToDesignElementsElement getRdal_traceabletodesignelementselement() {
        return rdal_traceabletodesignelementselement;
    }

    public void setRdal_traceabletodesignelementselement(rdal_TraceableToDesignElementsElement rdal_traceabletodesignelementselement) {
        this.rdal_traceabletodesignelementselement = rdal_traceabletodesignelementselement;
    }
    public List<rdal_ActorReference> getRdal_actorreferences() {
        return rdal_actorreferences;
    }

    public void addRdal_actorreference(Rdal_actorreference rdal_actorreference) {
        this.rdal_actorreferences.add(rdal_actorreference);
    }
    public List<rdal_Conflict> getRdal_conflicts() {
        return rdal_conflicts;
    }

    public void addRdal_conflict(Rdal_conflict rdal_conflict) {
        this.rdal_conflicts.add(rdal_conflict);
    }
    public List<rdal_RdalOrgPackage> getRdal_rdalorgpackages() {
        return rdal_rdalorgpackages;
    }

    public void addRdal_rdalorgpackage(Rdal_rdalorgpackage rdal_rdalorgpackage) {
        this.rdal_rdalorgpackages.add(rdal_rdalorgpackage);
    }
    public List<rdal_NonFunctionalProperty> getRdal_nonfunctionalpropertys() {
        return rdal_nonfunctionalpropertys;
    }

    public void addRdal_nonfunctionalproperty(Rdal_nonfunctionalproperty rdal_nonfunctionalproperty) {
        this.rdal_nonfunctionalpropertys.add(rdal_nonfunctionalproperty);
    }
    public List<rdal_ContactInformation> getRdal_contactinformations() {
        return rdal_contactinformations;
    }

    public void addRdal_contactinformation(Rdal_contactinformation rdal_contactinformation) {
        this.rdal_contactinformations.add(rdal_contactinformation);
    }

}