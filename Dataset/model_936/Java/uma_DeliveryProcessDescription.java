





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String riskLevel;
    private String projectCharacteristics;
    private String projectMemberExpertise;
    private String estimatingTechnique;
    private String typeOfContract;
    private String scale;



    public uma_DeliveryProcessDescription(
        String riskLevel,        String projectCharacteristics,        String projectMemberExpertise,        String estimatingTechnique,        String typeOfContract,        String scale    ) {
        super(
        );
        this.riskLevel = riskLevel;
        this.projectCharacteristics = projectCharacteristics;
        this.projectMemberExpertise = projectMemberExpertise;
        this.estimatingTechnique = estimatingTechnique;
        this.typeOfContract = typeOfContract;
        this.scale = scale;
    }


    public String getRisklevel() {
        return riskLevel;
    }

    public void setRisklevel(String riskLevel) {
        this.riskLevel = riskLevel;
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
    public String getEstimatingtechnique() {
        return estimatingTechnique;
    }

    public void setEstimatingtechnique(String estimatingTechnique) {
        this.estimatingTechnique = estimatingTechnique;
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


}