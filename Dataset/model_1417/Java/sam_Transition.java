





import java.util.List;
import java.util.ArrayList;

public class sam_Transition extends IdentifiedItem {

    private String priority;
    private String condition;
    private String emission;





    private sam_AbstractState sam_abstractstate;




    private sam_AbstractState sam_abstractstate;


    public sam_Transition(
        String priority,        String condition,        String emission    ) {
        super(
        );
        this.priority = priority;
        this.condition = condition;
        this.emission = emission;
    }


    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getEmission() {
        return emission;
    }

    public void setEmission(String emission) {
        this.emission = emission;
    }

    public sam_AbstractState getSam_abstractstate() {
        return sam_abstractstate;
    }

    public void setSam_abstractstate(sam_AbstractState sam_abstractstate) {
        this.sam_abstractstate = sam_abstractstate;
    }
    public sam_AbstractState getSam_abstractstate() {
        return sam_abstractstate;
    }

    public void setSam_abstractstate(sam_AbstractState sam_abstractstate) {
        this.sam_abstractstate = sam_abstractstate;
    }

}