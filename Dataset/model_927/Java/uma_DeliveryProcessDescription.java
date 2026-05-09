





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String scale;
    private String projectMemberExpertise;
    private String projectCharacteristics;
    private String typeOfContract;
    private String riskLevel;
    private String estimatingTechnique;



    public uma_DeliveryProcessDescription(
        String scale,        String projectMemberExpertise,        String projectCharacteristics,        String typeOfContract,        String riskLevel,        String estimatingTechnique    ) {
        super(
        );
        this.scale = scale;
        this.projectMemberExpertise = projectMemberExpertise;
        this.projectCharacteristics = projectCharacteristics;
        this.typeOfContract = typeOfContract;
        this.riskLevel = riskLevel;
        this.estimatingTechnique = estimatingTechnique;
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
    public String getProjectcharacteristics() {
        return projectCharacteristics;
    }

    public void setProjectcharacteristics(String projectCharacteristics) {
        this.projectCharacteristics = projectCharacteristics;
    }
    public String getTypeofcontract() {
        return typeOfContract;
    }

    public void setTypeofcontract(String typeOfContract) {
        this.typeOfContract = typeOfContract;
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


}