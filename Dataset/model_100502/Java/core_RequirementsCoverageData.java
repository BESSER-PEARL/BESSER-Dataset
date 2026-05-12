





import java.util.List;
import java.util.ArrayList;

public class core_RequirementsCoverageData extends IdentifiedElement {

    private String verificationLevel;
    private int nbRequirements;



    public core_RequirementsCoverageData(
        String verificationLevel,        int nbRequirements    ) {
        super(
        );
        this.verificationLevel = verificationLevel;
        this.nbRequirements = nbRequirements;
    }


    public String getVerificationlevel() {
        return verificationLevel;
    }

    public void setVerificationlevel(String verificationLevel) {
        this.verificationLevel = verificationLevel;
    }
    public int getNbrequirements() {
        return nbRequirements;
    }

    public void setNbrequirements(int nbRequirements) {
        this.nbRequirements = nbRequirements;
    }


}