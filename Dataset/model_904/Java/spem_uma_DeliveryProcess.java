





import java.util.List;
import java.util.ArrayList;

public class spem_uma_DeliveryProcess extends Process {

    private String typeOfContract;
    private String projectCharacteristics;
    private String riskLevel;
    private String estimatingTechnique;
    private String projectMemberExpertise;
    private String scale;



    public spem_uma_DeliveryProcess(
        String typeOfContract,        String projectCharacteristics,        String riskLevel,        String estimatingTechnique,        String projectMemberExpertise,        String scale    ) {
        super(
        );
        this.typeOfContract = typeOfContract;
        this.projectCharacteristics = projectCharacteristics;
        this.riskLevel = riskLevel;
        this.estimatingTechnique = estimatingTechnique;
        this.projectMemberExpertise = projectMemberExpertise;
        this.scale = scale;
    }


    public String getTypeofcontract() {
        return typeOfContract;
    }

    public void setTypeofcontract(String typeOfContract) {
        this.typeOfContract = typeOfContract;
    }
    public String getProjectcharacteristics() {
        return projectCharacteristics;
    }

    public void setProjectcharacteristics(String projectCharacteristics) {
        this.projectCharacteristics = projectCharacteristics;
    }
    public String getRisklevel() {
        return riskLevel;
    }

    public void setRisklevel(String riskLevel) {
        this.riskLevel = riskLevel;
    }
    public String getEstimatingtechnique() {
        return estimatingTechnique;
    }

    public void setEstimatingtechnique(String estimatingTechnique) {
        this.estimatingTechnique = estimatingTechnique;
    }
    public String getProjectmemberexpertise() {
        return projectMemberExpertise;
    }

    public void setProjectmemberexpertise(String projectMemberExpertise) {
        this.projectMemberExpertise = projectMemberExpertise;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }


}