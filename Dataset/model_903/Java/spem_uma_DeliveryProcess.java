





import java.util.List;
import java.util.ArrayList;

public class spem_uma_DeliveryProcess extends Process {

    private String typeOfContract;
    private String scale;
    private String estimatingTechnique;
    private String projectCharacteristics;
    private String riskLevel;
    private String projectMemberExpertise;



    public spem_uma_DeliveryProcess(
        String typeOfContract,        String scale,        String estimatingTechnique,        String projectCharacteristics,        String riskLevel,        String projectMemberExpertise    ) {
        super(
        );
        this.typeOfContract = typeOfContract;
        this.scale = scale;
        this.estimatingTechnique = estimatingTechnique;
        this.projectCharacteristics = projectCharacteristics;
        this.riskLevel = riskLevel;
        this.projectMemberExpertise = projectMemberExpertise;
    }


    public String getTypeofcontract() {
        return typeOfContract;
    }

    public void setTypeofcontract(String typeOfContract) {
        this.typeOfContract = typeOfContract;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getEstimatingtechnique() {
        return estimatingTechnique;
    }

    public void setEstimatingtechnique(String estimatingTechnique) {
        this.estimatingTechnique = estimatingTechnique;
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
    public String getProjectmemberexpertise() {
        return projectMemberExpertise;
    }

    public void setProjectmemberexpertise(String projectMemberExpertise) {
        this.projectMemberExpertise = projectMemberExpertise;
    }


}