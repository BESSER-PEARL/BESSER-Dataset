





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String projectCharacteristics;
    private String typeOfContract;
    private String scale;
    private String riskLevel;
    private String estimatingTechnique;
    private String projectMemberExpertise;



    public uma_DeliveryProcessDescription(
        String projectCharacteristics,        String typeOfContract,        String scale,        String riskLevel,        String estimatingTechnique,        String projectMemberExpertise    ) {
        super(
        );
        this.projectCharacteristics = projectCharacteristics;
        this.typeOfContract = typeOfContract;
        this.scale = scale;
        this.riskLevel = riskLevel;
        this.estimatingTechnique = estimatingTechnique;
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
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
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


}