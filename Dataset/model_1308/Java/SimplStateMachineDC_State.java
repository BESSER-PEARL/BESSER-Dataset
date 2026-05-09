





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachineDC_State  {

    private String OrdIf;
    private String name;
    private boolean isActive;
    private String Ord;
    private String Inh;
    private String InhIf;





    private SimplStateMachineDC_Transition simplstatemachinedc_transition;




    private SimplStateMachineDC_Transition simplstatemachinedc_transition;




    private SimplStateMachineDC_StateMachine simplstatemachinedc_statemachine;


    public SimplStateMachineDC_State(
        String OrdIf,        String name,        boolean isActive,        String Ord,        String Inh,        String InhIf    ) {
        this.OrdIf = OrdIf;
        this.name = name;
        this.isActive = isActive;
        this.Ord = Ord;
        this.Inh = Inh;
        this.InhIf = InhIf;
    }


    public String getOrdif() {
        return OrdIf;
    }

    public void setOrdif(String OrdIf) {
        this.OrdIf = OrdIf;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public String getOrd() {
        return Ord;
    }

    public void setOrd(String Ord) {
        this.Ord = Ord;
    }
    public String getInh() {
        return Inh;
    }

    public void setInh(String Inh) {
        this.Inh = Inh;
    }
    public String getInhif() {
        return InhIf;
    }

    public void setInhif(String InhIf) {
        this.InhIf = InhIf;
    }

    public SimplStateMachineDC_Transition getSimplstatemachinedc_transition() {
        return simplstatemachinedc_transition;
    }

    public void setSimplstatemachinedc_transition(SimplStateMachineDC_Transition simplstatemachinedc_transition) {
        this.simplstatemachinedc_transition = simplstatemachinedc_transition;
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

}