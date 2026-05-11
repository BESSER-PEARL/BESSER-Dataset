





import java.util.List;
import java.util.ArrayList;

public class urml_Transition  {

    private boolean universal;
    private boolean init;
    private String name;





    private urml_TimerPort urml_timerport;




    private urml_StateMachine urml_statemachine;




    private urml_State_ urml_state_;




    private List<urml_Trigger_in> urml_trigger_ins;




    private urml_State_ urml_state_;




    private urml_Expression urml_expression;


    public urml_Transition(
        boolean universal,        boolean init,        String name    ) {
        this.universal = universal;
        this.init = init;
        this.name = name;
        this.urml_trigger_ins = new ArrayList<>();
    }

    public urml_Transition(
        boolean universal,        boolean init,        String name        ArrayList<urml_Trigger_in> urml_trigger_ins    ) {
        this.universal = universal;
        this.init = init;
        this.name = name;
        this.urml_trigger_ins = urml_trigger_ins;
    }

    public boolean getUniversal() {
        return universal;
    }

    public void setUniversal(boolean universal) {
        this.universal = universal;
    }
    public boolean getInit() {
        return init;
    }

    public void setInit(boolean init) {
        this.init = init;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public urml_TimerPort getUrml_timerport() {
        return urml_timerport;
    }

    public void setUrml_timerport(urml_TimerPort urml_timerport) {
        this.urml_timerport = urml_timerport;
    }
    public urml_StateMachine getUrml_statemachine() {
        return urml_statemachine;
    }

    public void setUrml_statemachine(urml_StateMachine urml_statemachine) {
        this.urml_statemachine = urml_statemachine;
    }
    public urml_State_ getUrml_state_() {
        return urml_state_;
    }

    public void setUrml_state_(urml_State_ urml_state_) {
        this.urml_state_ = urml_state_;
    }
    public List<urml_Trigger_in> getUrml_trigger_ins() {
        return urml_trigger_ins;
    }

    public void addUrml_trigger_in(Urml_trigger_in urml_trigger_in) {
        this.urml_trigger_ins.add(urml_trigger_in);
    }
    public urml_State_ getUrml_state_() {
        return urml_state_;
    }

    public void setUrml_state_(urml_State_ urml_state_) {
        this.urml_state_ = urml_state_;
    }
    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }

}