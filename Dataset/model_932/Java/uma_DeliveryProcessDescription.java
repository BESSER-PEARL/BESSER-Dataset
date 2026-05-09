





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcessDescription extends ProcessDescription {

    private String estimatingTechnique;
    private String scale;
    private String projectCharacteristics;
    private String projectMemberExpertise;
    private String riskLevel;
    private String typeOfContract;



    public uma_DeliveryProcessDescription(
        String estimatingTechnique,        String scale,        String projectCharacteristics,        String projectMemberExpertise,        String riskLevel,        String typeOfContract    ) {
        super(
        );
        this.estimatingTechnique = estimatingTechnique;
        this.scale = scale;
        this.projectCharacteristics = projectCharacteristics;
        this.projectMemberExpertise = projectMemberExpertise;
        this.riskLevel = riskLevel;
        this.typeOfContract = typeOfContract;
    }


    public String getEstimatingtechnique() {
        return estimatingTechnique;
    }

    public void setEstimatingtechnique(String estimatingTechnique) {
        this.estimatingTechnique = estimatingTechnique;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
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


}