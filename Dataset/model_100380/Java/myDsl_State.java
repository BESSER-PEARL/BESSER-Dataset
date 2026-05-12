





import java.util.List;
import java.util.ArrayList;

public class myDsl_State  {

    private String name;





    private List<myDsl_Transition> mydsl_transitions;




    private myDsl_Transition mydsl_transition;




    private myDsl_XExpression mydsl_xexpression;




    private myDsl_Statemachine mydsl_statemachine;


    public myDsl_State(
        String name    ) {
        this.name = name;
        this.mydsl_transitions = new ArrayList<>();
    }

    public myDsl_State(
        String name        ArrayList<myDsl_Transition> mydsl_transitions    ) {
        this.name = name;
        this.mydsl_transitions = mydsl_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<myDsl_Transition> getMydsl_transitions() {
        return mydsl_transitions;
    }

    public void addMydsl_transition(Mydsl_transition mydsl_transition) {
        this.mydsl_transitions.add(mydsl_transition);
    }
    public myDsl_Transition getMydsl_transition() {
        return mydsl_transition;
    }

    public void setMydsl_transition(myDsl_Transition mydsl_transition) {
        this.mydsl_transition = mydsl_transition;
    }
    public myDsl_XExpression getMydsl_xexpression() {
        return mydsl_xexpression;
    }

    public void setMydsl_xexpression(myDsl_XExpression mydsl_xexpression) {
        this.mydsl_xexpression = mydsl_xexpression;
    }
    public myDsl_Statemachine getMydsl_statemachine() {
        return mydsl_statemachine;
    }

    public void setMydsl_statemachine(myDsl_Statemachine mydsl_statemachine) {
        this.mydsl_statemachine = mydsl_statemachine;
    }

}