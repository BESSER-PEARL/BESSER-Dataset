





import java.util.List;
import java.util.ArrayList;

public class rdal_RdalOrgPackage extends IdentifiedElement {

    private String refinementEntries;
    private String contractualElementEntries;





    private List<rdal_ElementRefinement> rdal_elementrefinements;




    private rdal_RdalOrgPackage rdal_rdalorgpackage;




    private rdal_RdalOrgPackage rdal_rdalorgpackage;


    public rdal_RdalOrgPackage(
        String refinementEntries,        String contractualElementEntries    ) {
        super(
        );
        this.refinementEntries = refinementEntries;
        this.contractualElementEntries = contractualElementEntries;
        this.rdal_elementrefinements = new ArrayList<>();
    }

    public rdal_RdalOrgPackage(
        String refinementEntries,        String contractualElementEntries        ArrayList<rdal_ElementRefinement> rdal_elementrefinements    ) {
        this.refinementEntries = refinementEntries;
        this.contractualElementEntries = contractualElementEntries;
        this.rdal_elementrefinements = rdal_elementrefinements;
    }

    public String getRefinemententries() {
        return refinementEntries;
    }

    public void setRefinemententries(String refinementEntries) {
        this.refinementEntries = refinementEntries;
    }
    public String getContractualelemententries() {
        return contractualElementEntries;
    }

    public void setContractualelemententries(String contractualElementEntries) {
        this.contractualElementEntries = contractualElementEntries;
    }

    public List<rdal_ElementRefinement> getRdal_elementrefinements() {
        return rdal_elementrefinements;
    }

    public void addRdal_elementrefinement(Rdal_elementrefinement rdal_elementrefinement) {
        this.rdal_elementrefinements.add(rdal_elementrefinement);
    }
    public rdal_RdalOrgPackage getRdal_rdalorgpackage() {
        return rdal_rdalorgpackage;
    }

    public void setRdal_rdalorgpackage(rdal_RdalOrgPackage rdal_rdalorgpackage) {
        this.rdal_rdalorgpackage = rdal_rdalorgpackage;
    }
    public rdal_RdalOrgPackage getRdal_rdalorgpackage() {
        return rdal_rdalorgpackage;
    }

    public void setRdal_rdalorgpackage(rdal_RdalOrgPackage rdal_rdalorgpackage) {
        this.rdal_rdalorgpackage = rdal_rdalorgpackage;
    }

}