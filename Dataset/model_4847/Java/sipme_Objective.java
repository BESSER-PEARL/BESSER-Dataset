





import java.util.List;
import java.util.ArrayList;

public class sipme_Objective extends EnterpriseObject {

    private String objectiveNature;
    private String objectiveType;





    private sipme_Objective sipme_objective;




    private List<sipme_Objective> sipme_objectives;


    public sipme_Objective(
        String objectiveNature,        String objectiveType    ) {
        super(
        );
        this.objectiveNature = objectiveNature;
        this.objectiveType = objectiveType;
        this.sipme_objectives = new ArrayList<>();
    }

    public sipme_Objective(
        String objectiveNature,        String objectiveType        ArrayList<sipme_Objective> sipme_objectives    ) {
        this.objectiveNature = objectiveNature;
        this.objectiveType = objectiveType;
        this.sipme_objectives = sipme_objectives;
    }

    public String getObjectivenature() {
        return objectiveNature;
    }

    public void setObjectivenature(String objectiveNature) {
        this.objectiveNature = objectiveNature;
    }
    public String getObjectivetype() {
        return objectiveType;
    }

    public void setObjectivetype(String objectiveType) {
        this.objectiveType = objectiveType;
    }

    public sipme_Objective getSipme_objective() {
        return sipme_objective;
    }

    public void setSipme_objective(sipme_Objective sipme_objective) {
        this.sipme_objective = sipme_objective;
    }
    public List<sipme_Objective> getSipme_objectives() {
        return sipme_objectives;
    }

    public void addSipme_objective(Sipme_objective sipme_objective) {
        this.sipme_objectives.add(sipme_objective);
    }

}