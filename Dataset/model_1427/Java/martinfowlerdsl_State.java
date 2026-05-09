





import java.util.List;
import java.util.ArrayList;

public class martinfowlerdsl_State  {

    private String name;





    private List<martinfowlerdsl_Transition> martinfowlerdsl_transitions;




    private martinfowlerdsl_StateMachine martinfowlerdsl_statemachine;




    private List<martinfowlerdsl_Command> martinfowlerdsl_commands;




    private martinfowlerdsl_Transition martinfowlerdsl_transition;




    private martinfowlerdsl_StateMachine martinfowlerdsl_statemachine;




    private martinfowlerdsl_Transition martinfowlerdsl_transition;


    public martinfowlerdsl_State(
        String name    ) {
        this.name = name;
        this.martinfowlerdsl_transitions = new ArrayList<>();
        this.martinfowlerdsl_commands = new ArrayList<>();
    }

    public martinfowlerdsl_State(
        String name        ArrayList<martinfowlerdsl_Transition> martinfowlerdsl_transitions,        ArrayList<martinfowlerdsl_Command> martinfowlerdsl_commands    ) {
        this.name = name;
        this.martinfowlerdsl_transitions = martinfowlerdsl_transitions;
        this.martinfowlerdsl_commands = martinfowlerdsl_commands;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<martinfowlerdsl_Transition> getMartinfowlerdsl_transitions() {
        return martinfowlerdsl_transitions;
    }

    public void addMartinfowlerdsl_transition(Martinfowlerdsl_transition martinfowlerdsl_transition) {
        this.martinfowlerdsl_transitions.add(martinfowlerdsl_transition);
    }
    public martinfowlerdsl_StateMachine getMartinfowlerdsl_statemachine() {
        return martinfowlerdsl_statemachine;
    }

    public void setMartinfowlerdsl_statemachine(martinfowlerdsl_StateMachine martinfowlerdsl_statemachine) {
        this.martinfowlerdsl_statemachine = martinfowlerdsl_statemachine;
    }
    public List<martinfowlerdsl_Command> getMartinfowlerdsl_commands() {
        return martinfowlerdsl_commands;
    }

    public void addMartinfowlerdsl_command(Martinfowlerdsl_command martinfowlerdsl_command) {
        this.martinfowlerdsl_commands.add(martinfowlerdsl_command);
    }
    public martinfowlerdsl_Transition getMartinfowlerdsl_transition() {
        return martinfowlerdsl_transition;
    }

    public void setMartinfowlerdsl_transition(martinfowlerdsl_Transition martinfowlerdsl_transition) {
        this.martinfowlerdsl_transition = martinfowlerdsl_transition;
    }
    public martinfowlerdsl_StateMachine getMartinfowlerdsl_statemachine() {
        return martinfowlerdsl_statemachine;
    }

    public void setMartinfowlerdsl_statemachine(martinfowlerdsl_StateMachine martinfowlerdsl_statemachine) {
        this.martinfowlerdsl_statemachine = martinfowlerdsl_statemachine;
    }
    public martinfowlerdsl_Transition getMartinfowlerdsl_transition() {
        return martinfowlerdsl_transition;
    }

    public void setMartinfowlerdsl_transition(martinfowlerdsl_Transition martinfowlerdsl_transition) {
        this.martinfowlerdsl_transition = martinfowlerdsl_transition;
    }

}