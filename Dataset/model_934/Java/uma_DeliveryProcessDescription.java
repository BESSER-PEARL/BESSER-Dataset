





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String typeOfContract;
    private String riskLevel;
    private String estimatingTechnique;
    private String projectCharacteristics;
    private String projectMemberExpertise;
    private String scale;



    public uma_DeliveryProcessDescription(
        String typeOfContract,        String riskLevel,        String estimatingTechnique,        String projectCharacteristics,        String projectMemberExpertise,        String scale    ) {
        super(
        );
        this.typeOfContract = typeOfContract;
        this.riskLevel = riskLevel;
        this.estimatingTechnique = estimatingTechnique;
        this.projectCharacteristics = projectCharacteristics;
        this.projectMemberExpertise = projectMemberExpertise;
        this.scale = scale;
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
    public String getProjectcharacteristics() {
        return projectCharacteristics;
    }

    public void setProjectcharacteristics(String projectCharacteristics) {
        this.projectCharacteristics = projectCharacteristics;
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