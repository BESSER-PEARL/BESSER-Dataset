





import java.util.List;
import java.util.ArrayList;

public class core_RequirementsCoverageData extends IdentifiedElement {

    private int nbRequirements;
    private String verificationLevel;



    public core_RequirementsCoverageData(
        int nbRequirements,        String verificationLevel    ) {
        super(
        );
        this.nbRequirements = nbRequirements;
        this.verificationLevel = verificationLevel;
    }


    public int getNbrequirements() {
        return nbRequirements;
    }

    public void setNbrequirements(int nbRequirements) {
        this.nbRequirements = nbRequirements;
    }
    public String getVerificationlevel() {
        return verificationLevel;
    }

    public void setVerificationlevel(String verificationLevel) {
        this.verificationLevel = verificationLevel;
    }


}