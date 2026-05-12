





import java.util.List;
import java.util.ArrayList;

public class rdal_SystemOverview extends AbstractContractualElement {

    private String purpose;





    private List<rdal_Capability> rdal_capabilitys;




    private List<rdal_SystemContext> rdal_systemcontexts;




    private rdal_Specification rdal_specification;




    private rdal_SystemContext rdal_systemcontext;


    public rdal_SystemOverview(
        String purpose    ) {
        super(
        );
        this.purpose = purpose;
        this.rdal_capabilitys = new ArrayList<>();
        this.rdal_systemcontexts = new ArrayList<>();
    }

    public rdal_SystemOverview(
        String purpose        ArrayList<rdal_Capability> rdal_capabilitys,        ArrayList<rdal_SystemContext> rdal_systemcontexts    ) {
        this.purpose = purpose;
        this.rdal_capabilitys = rdal_capabilitys;
        this.rdal_systemcontexts = rdal_systemcontexts;
    }

    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }

    public List<rdal_Capability> getRdal_capabilitys() {
        return rdal_capabilitys;
    }

    public void addRdal_capability(Rdal_capability rdal_capability) {
        this.rdal_capabilitys.add(rdal_capability);
    }
    public List<rdal_SystemContext> getRdal_systemcontexts() {
        return rdal_systemcontexts;
    }

    public void addRdal_systemcontext(Rdal_systemcontext rdal_systemcontext) {
        this.rdal_systemcontexts.add(rdal_systemcontext);
    }
    public rdal_Specification getRdal_specification() {
        return rdal_specification;
    }

    public void setRdal_specification(rdal_Specification rdal_specification) {
        this.rdal_specification = rdal_specification;
    }
    public rdal_SystemContext getRdal_systemcontext() {
        return rdal_systemcontext;
    }

    public void setRdal_systemcontext(rdal_SystemContext rdal_systemcontext) {
        this.rdal_systemcontext = rdal_systemcontext;
    }

}