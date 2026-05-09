





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String scale;
    private String estimatingTechnique;
    private String projectCharacteristics;
    private String typeOfContract;
    private String projectMemberExpertise;
    private String riskLevel;



    public uma_DeliveryProcessDescription(
        String scale,        String estimatingTechnique,        String projectCharacteristics,        String typeOfContract,        String projectMemberExpertise,        String riskLevel    ) {
        super(
        );
        this.scale = scale;
        this.estimatingTechnique = estimatingTechnique;
        this.projectCharacteristics = projectCharacteristics;
        this.typeOfContract = typeOfContract;
        this.projectMemberExpertise = projectMemberExpertise;
        this.riskLevel = riskLevel;
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
    public String getRisklevel() {
        return riskLevel;
    }

    public void setRisklevel(String riskLevel) {
        this.riskLevel = riskLevel;
    }


}