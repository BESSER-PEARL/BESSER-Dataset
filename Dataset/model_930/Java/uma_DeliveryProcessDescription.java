





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String typeOfContract;
    private String projectMemberExpertise;
    private String projectCharacteristics;
    private String estimatingTechnique;
    private String riskLevel;
    private String scale;



    public uma_DeliveryProcessDescription(
        String typeOfContract,        String projectMemberExpertise,        String projectCharacteristics,        String estimatingTechnique,        String riskLevel,        String scale    ) {
        super(
        );
        this.typeOfContract = typeOfContract;
        this.projectMemberExpertise = projectMemberExpertise;
        this.projectCharacteristics = projectCharacteristics;
        this.estimatingTechnique = estimatingTechnique;
        this.riskLevel = riskLevel;
        this.scale = scale;
    }


    public String getTypeofcontract() {
        return typeOfContract;
    }

    public void setTypeofcontract(String typeOfContract) {
        this.typeOfContract = typeOfContract;
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
    public String getEstimatingtechnique() {
        return estimatingTechnique;
    }

    public void setEstimatingtechnique(String estimatingTechnique) {
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


}