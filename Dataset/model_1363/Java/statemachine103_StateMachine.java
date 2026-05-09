





import java.util.List;
import java.util.ArrayList;

public class statemachine103_StateMachine  {

    private String label;





    private List<statemachine103_StateMachineVariable> statemachine103_statemachinevariables;


    public statemachine103_StateMachine(
        String label    ) {
        this.label = label;
        this.statemachine103_statemachinevariables = new ArrayList<>();
    }

    public statemachine103_StateMachine(
        String label        ArrayList<statemachine103_StateMachineVariable> statemachine103_statemachinevariables    ) {
        this.label = label;
        this.statemachine103_statemachinevariables = statemachine103_statemachinevariables;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<statemachine103_StateMachineVariable> getStatemachine103_statemachinevariables() {
        return statemachine103_statemachinevariables;
    }

    public void addStatemachine103_statemachinevariable(Statemachine103_statemachinevariable statemachine103_statemachinevariable) {
        this.statemachine103_statemachinevariables.add(statemachine103_statemachinevariable);
    }

}