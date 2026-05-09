





import java.util.List;
import java.util.ArrayList;

public class sam_Transition extends TraceableElement {

    private String condition;
    private String emission;
    private String priority;





    private sam_State sam_state;




    private sam_Automaton sam_automaton;




    private sam_State sam_state;




    private sam_Automaton sam_automaton;


    public sam_Transition(
        String condition,        String emission,        String priority    ) {
        super(
        );
        this.condition = condition;
        this.emission = emission;
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
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public sam_State getSam_state() {
        return sam_state;
    }

    public void setSam_state(sam_State sam_state) {
        this.sam_state = sam_state;
    }
    public sam_Automaton getSam_automaton() {
        return sam_automaton;
    }

    public void setSam_automaton(sam_Automaton sam_automaton) {
        this.sam_automaton = sam_automaton;
    }
    public sam_State getSam_state() {
        return sam_state;
    }

    public void setSam_state(sam_State sam_state) {
        this.sam_state = sam_state;
    }
    public sam_Automaton getSam_automaton() {
        return sam_automaton;
    }

    public void setSam_automaton(sam_Automaton sam_automaton) {
        this.sam_automaton = sam_automaton;
    }

}