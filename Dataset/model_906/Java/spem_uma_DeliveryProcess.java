





import java.util.List;
import java.util.ArrayList;

public class spem_uma_DeliveryProcess extends Process {

    private String riskLevel;
    private String scale;
    private String projectMemberExpertise;
    private String typeOfContract;
    private String projectCharacteristics;
    private String estimatingTechnique;



    public spem_uma_DeliveryProcess(
        String riskLevel,        String scale,        String projectMemberExpertise,        String typeOfContract,        String projectCharacteristics,        String estimatingTechnique    ) {
        super(
        );
        this.riskLevel = riskLevel;
        this.scale = scale;
        this.projectMemberExpertise = projectMemberExpertise;
        this.typeOfContract = typeOfContract;
        this.projectCharacteristics = projectCharacteristics;
        this.estimatingTechnique = estimatingTechnique;
    }


    public String getRisklevel() {
        return riskLevel;
    }

    public void setRisklevel(String riskLevel) {
        this.riskLevel = riskLevel;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getProjectmemberexpertise() {
        return projectMemberExpertise;
    }

    public void setProjectmemberexpertise(String projectMemberExpertise) {
        this.projectMemberExpertise = projectMemberExpertise;
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
    public String getEstimatingtechnique() {
        return estimatingTechnique;
    }

    public void setEstimatingtechnique(String estimatingTechnique) {
        this.estimatingTechnique = estimatingTechnique;
    }


}