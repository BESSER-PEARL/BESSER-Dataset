





import java.util.List;
import java.util.ArrayList;

public class rdal_AbstractRequirement extends TextualContractualElement, SatisfiableElement, VerifiableElement {

    private String risk;





    private rdal_RequirementsPackage rdal_requirementspackage;




    private List<rdal_VerificationActivity> rdal_verificationactivitys;




    private rdal_RequirementRefinement rdal_requirementrefinement;




    private rdal_RequirementRefinement rdal_requirementrefinement;




    private rdal_RequirementsPackage rdal_requirementspackage;




    private rdal_VerificationActivity rdal_verificationactivity;


    public rdal_AbstractRequirement(
        String risk    ) {
        super(
        );
        this.risk = risk;
        this.rdal_verificationactivitys = new ArrayList<>();
    }

    public rdal_AbstractRequirement(
        String risk        ArrayList<rdal_VerificationActivity> rdal_verificationactivitys    ) {
        this.risk = risk;
        this.rdal_verificationactivitys = rdal_verificationactivitys;
    }

    public String getRisk() {
        return risk;
    }

    public void setRisk(String risk) {
        this.risk = risk;
    }

    public rdal_RequirementsPackage getRdal_requirementspackage() {
        return rdal_requirementspackage;
    }

    public void setRdal_requirementspackage(rdal_RequirementsPackage rdal_requirementspackage) {
        this.rdal_requirementspackage = rdal_requirementspackage;
    }
    public List<rdal_VerificationActivity> getRdal_verificationactivitys() {
        return rdal_verificationactivitys;
    }

    public void addRdal_verificationactivity(Rdal_verificationactivity rdal_verificationactivity) {
        this.rdal_verificationactivitys.add(rdal_verificationactivity);
    }
    public rdal_RequirementRefinement getRdal_requirementrefinement() {
        return rdal_requirementrefinement;
    }

    public void setRdal_requirementrefinement(rdal_RequirementRefinement rdal_requirementrefinement) {
        this.rdal_requirementrefinement = rdal_requirementrefinement;
    }
    public rdal_RequirementRefinement getRdal_requirementrefinement() {
        return rdal_requirementrefinement;
    }

    public void setRdal_requirementrefinement(rdal_RequirementRefinement rdal_requirementrefinement) {
        this.rdal_requirementrefinement = rdal_requirementrefinement;
    }
    public rdal_RequirementsPackage getRdal_requirementspackage() {
        return rdal_requirementspackage;
    }

    public void setRdal_requirementspackage(rdal_RequirementsPackage rdal_requirementspackage) {
        this.rdal_requirementspackage = rdal_requirementspackage;
    }
    public rdal_VerificationActivity getRdal_verificationactivity() {
        return rdal_verificationactivity;
    }

    public void setRdal_verificationactivity(rdal_VerificationActivity rdal_verificationactivity) {
        this.rdal_verificationactivity = rdal_verificationactivity;
    }

}