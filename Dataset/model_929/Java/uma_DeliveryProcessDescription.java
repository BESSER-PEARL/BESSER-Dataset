





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String riskLevel;
    private String typeOfContract;
    private String estimatingTechnique;
    private String projectCharacteristics;
    private String scale;
    private String projectMemberExpertise;



    public uma_DeliveryProcessDescription(
        String riskLevel,        String typeOfContract,        String estimatingTechnique,        String projectCharacteristics,        String scale,        String projectMemberExpertise    ) {
        super(
        );
        this.riskLevel = riskLevel;
        this.typeOfContract = typeOfContract;
        this.estimatingTechnique = estimatingTechnique;
        this.projectCharacteristics = projectCharacteristics;
        this.scale = scale;
        this.projectMemberExpertise = projectMemberExpertise;
    }


    public String getRisklevel() {
        return riskLevel;
    }

    public void setRisklevel(String riskLevel) {
        this.riskLevel = riskLevel;
    }
    public String getTypeofcontract() {
        return typeOfContract;
    }

    public void setTypeofcontract(String typeOfContract) {
        this.typeOfContract = typeOfContract;
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


}