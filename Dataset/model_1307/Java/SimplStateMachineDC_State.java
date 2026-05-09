





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachineDC_State  {

    private String Inh;
    private String name;
    private String OrdIf;
    private String Ord;
    private String InhIf;
    private boolean isActive;





    private SimplStateMachineDC_Transition simplstatemachinedc_transition;




    private SimplStateMachineDC_StateMachine simplstatemachinedc_statemachine;




    private SimplStateMachineDC_PseudoState simplstatemachinedc_pseudostate;




    private SimplStateMachineDC_Transition simplstatemachinedc_transition;


    public SimplStateMachineDC_State(
        String Inh,        String name,        String OrdIf,        String Ord,        String InhIf,        boolean isActive    ) {
        this.Inh = Inh;
        this.name = name;
        this.OrdIf = OrdIf;
        this.Ord = Ord;
        this.InhIf = InhIf;
        this.isActive = isActive;
    }


    public String getInh() {
        return Inh;
    }

    public void setInh(String Inh) {
        this.Inh = Inh;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOrdif() {
        return OrdIf;
    }

    public void setOrdif(String OrdIf) {
        this.OrdIf = OrdIf;
    }
    public String getOrd() {
        return Ord;
    }

    public void setOrd(String Ord) {
        this.Ord = Ord;
    }
    public String getInhif() {
        return InhIf;
    }

    public void setInhif(String InhIf) {
        this.InhIf = InhIf;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public SimplStateMachineDC_Transition getSimplstatemachinedc_transition() {
        return simplstatemachinedc_transition;
    }

    public void setSimplstatemachinedc_transition(SimplStateMachineDC_Transition simplstatemachinedc_transition) {
        this.simplstatemachinedc_transition = simplstatemachinedc_transition;
    }
    public SimplStateMachineDC_StateMachine getSimplstatemachinedc_statemachine() {
        return simplstatemachinedc_statemachine;
    }

    public void setSimplstatemachinedc_statemachine(SimplStateMachineDC_StateMachine simplstatemachinedc_statemachine) {
        this.simplstatemachinedc_statemachine = simplstatemachinedc_statemachine;
    }
    public SimplStateMachineDC_PseudoState getSimplstatemachinedc_pseudostate() {
        return simplstatemachinedc_pseudostate;
    }

    public void setSimplstatemachinedc_pseudostate(SimplStateMachineDC_PseudoState simplstatemachinedc_pseudostate) {
        this.simplstatemachinedc_pseudostate = simplstatemachinedc_pseudostate;
    }
    public SimplStateMachineDC_Transition getSimplstatemachinedc_transition() {
        return simplstatemachinedc_transition;
    }

    public void setSimplstatemachinedc_transition(SimplStateMachineDC_Transition simplstatemachinedc_transition) {
        this.simplstatemachinedc_transition = simplstatemachinedc_transition;
    }

}