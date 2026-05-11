





import java.util.List;
import java.util.ArrayList;

public class cbmg_Transition  {

    private float probability;
    private String accept;
    private int nbrOfTransitions;
    private String condition;
    private float thinkTime;
    private String method;





    private cbmg_State cbmg_state;




    private cbmg_State cbmg_state;




    private cbmg_State cbmg_state;




    private cbmg_State cbmg_state;


    public cbmg_Transition(
        float probability,        String accept,        int nbrOfTransitions,        String condition,        float thinkTime,        String method    ) {
        this.probability = probability;
        this.accept = accept;
        this.nbrOfTransitions = nbrOfTransitions;
        this.condition = condition;
        this.thinkTime = thinkTime;
        this.method = method;
    }


    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public String getAccept() {
        return accept;
    }

    public void setAccept(String accept) {
        this.accept = accept;
    }
    public int getNbroftransitions() {
        return nbrOfTransitions;
    }

    public void setNbroftransitions(int nbrOfTransitions) {
        this.nbrOfTransitions = nbrOfTransitions;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public float getThinktime() {
        return thinkTime;
    }

    public void setThinktime(float thinkTime) {
        this.thinkTime = thinkTime;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public cbmg_State getCbmg_state() {
        return cbmg_state;
    }

    public void setCbmg_state(cbmg_State cbmg_state) {
        this.cbmg_state = cbmg_state;
    }
    public cbmg_State getCbmg_state() {
        return cbmg_state;
    }

    public void setCbmg_state(cbmg_State cbmg_state) {
        this.cbmg_state = cbmg_state;
    }
    public cbmg_State getCbmg_state() {
        return cbmg_state;
    }

    public void setCbmg_state(cbmg_State cbmg_state) {
        this.cbmg_state = cbmg_state;
    }
    public cbmg_State getCbmg_state() {
        return cbmg_state;
    }

    public void setCbmg_state(cbmg_State cbmg_state) {
        this.cbmg_state = cbmg_state;
    }

}