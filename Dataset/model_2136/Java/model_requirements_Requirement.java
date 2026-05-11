





import java.util.List;
import java.util.ArrayList;

public class model_requirements_Requirement extends base_IExternal, base_ISpecmateModelObject {

    private String status;
    private String plannedRelease;
    private boolean isRegressionRequirement;
    private int numberOfTests;
    private String implementingITTeam;
    private String platform;
    private String tac;
    private String implementingBOTeam;
    private String implementingUnit;



    public model_requirements_Requirement(
        String status,        String plannedRelease,        boolean isRegressionRequirement,        int numberOfTests,        String implementingITTeam,        String platform,        String tac,        String implementingBOTeam,        String implementingUnit    ) {
        super(
        );
        this.status = status;
        this.plannedRelease = plannedRelease;
        this.isRegressionRequirement = isRegressionRequirement;
        this.numberOfTests = numberOfTests;
        this.implementingITTeam = implementingITTeam;
        this.platform = platform;
        this.tac = tac;
        this.implementingBOTeam = implementingBOTeam;
        this.implementingUnit = implementingUnit;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getPlannedrelease() {
        return plannedRelease;
    }

    public void setPlannedrelease(String plannedRelease) {
        this.plannedRelease = plannedRelease;
    }
    public boolean getIsregressionrequirement() {
        return isRegressionRequirement;
    }

    public void setIsregressionrequirement(boolean isRegressionRequirement) {
        this.isRegressionRequirement = isRegressionRequirement;
    }
    public int getNumberoftests() {
        return numberOfTests;
    }

    public void setNumberoftests(int numberOfTests) {
        this.numberOfTests = numberOfTests;
    }
    public String getImplementingitteam() {
        return implementingITTeam;
    }

    public void setImplementingitteam(String implementingITTeam) {
        this.implementingITTeam = implementingITTeam;
    }
    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }
    public String getTac() {
        return tac;
    }

    public void setTac(String tac) {
        this.tac = tac;
    }
    public String getImplementingboteam() {
        return implementingBOTeam;
    }

    public void setImplementingboteam(String implementingBOTeam) {
        this.implementingBOTeam = implementingBOTeam;
    }
    public String getImplementingunit() {
        return implementingUnit;
    }

    public void setImplementingunit(String implementingUnit) {
        this.implementingUnit = implementingUnit;
    }


}