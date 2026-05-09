





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachineDC_CompositeState extends State {






    private List<SimplStateMachineDC_State> simplstatemachinedc_states;




    private SimplStateMachineDC_State simplstatemachinedc_state;


    public SimplStateMachineDC_CompositeState(
    ) {
        super(
        );
        this.simplstatemachinedc_states = new ArrayList<>();
    }

    public SimplStateMachineDC_CompositeState(
        ArrayList<SimplStateMachineDC_State> simplstatemachinedc_states    ) {
        this.simplstatemachinedc_states = simplstatemachinedc_states;
    }


    public List<SimplStateMachineDC_State> getSimplstatemachinedc_states() {
        return simplstatemachinedc_states;
    }

    public void addSimplstatemachinedc_state(Simplstatemachinedc_state simplstatemachinedc_state) {
        this.simplstatemachinedc_states.add(simplstatemachinedc_state);
    }
    public SimplStateMachineDC_State getSimplstatemachinedc_state() {
        return simplstatemachinedc_state;
    }

    public void setSimplstatemachinedc_state(SimplStateMachineDC_State simplstatemachinedc_state) {
        this.simplstatemachinedc_state = simplstatemachinedc_state;
    }

}