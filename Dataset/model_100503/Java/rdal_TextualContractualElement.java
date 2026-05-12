





import java.util.List;
import java.util.ArrayList;

public class rdal_TextualContractualElement extends AbstractContractualElement {

    private String priority;





    private List<rdal_TextualContractualElement> rdal_textualcontractualelements;




    private rdal_RdalOrgPackage rdal_rdalorgpackage;


    public rdal_TextualContractualElement(
        String priority    ) {
        super(
        );
        this.priority = priority;
        this.rdal_textualcontractualelements = new ArrayList<>();
    }

    public rdal_TextualContractualElement(
        String priority        ArrayList<rdal_TextualContractualElement> rdal_textualcontractualelements    ) {
        this.priority = priority;
        this.rdal_textualcontractualelements = rdal_textualcontractualelements;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public List<rdal_TextualContractualElement> getRdal_textualcontractualelements() {
        return rdal_textualcontractualelements;
    }

    public void addRdal_textualcontractualelement(Rdal_textualcontractualelement rdal_textualcontractualelement) {
        this.rdal_textualcontractualelements.add(rdal_textualcontractualelement);
    }
    public rdal_RdalOrgPackage getRdal_rdalorgpackage() {
        return rdal_rdalorgpackage;
    }

    public void setRdal_rdalorgpackage(rdal_RdalOrgPackage rdal_rdalorgpackage) {
        this.rdal_rdalorgpackage = rdal_rdalorgpackage;
    }

}