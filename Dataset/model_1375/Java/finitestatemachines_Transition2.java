





import java.util.List;
import java.util.ArrayList;

public class finitestatemachines_Transition2 extends NamedElement {

    private int initialTime;
    private int finalTime2;





    private finitestatemachines_StateMachine finitestatemachines_statemachine;




    private finitestatemachines_Trigger2 finitestatemachines_trigger2;




    private finitestatemachines_StateMachine finitestatemachines_statemachine;


    public finitestatemachines_Transition2(
        int initialTime,        int finalTime2    ) {
        super(
        );
        this.initialTime = initialTime;
        this.finalTime2 = finalTime2;
    }


    public int getInitialtime() {
        return initialTime;
    }

    public void setInitialtime(int initialTime) {
        this.initialTime = initialTime;
    }
    public int getFinaltime2() {
        return finalTime2;
    }

    public void setFinaltime2(int finalTime2) {
        this.finalTime2 = finalTime2;
    }

    public finitestatemachines_StateMachine getFinitestatemachines_statemachine() {
        return finitestatemachines_statemachine;
    }

    public void setFinitestatemachines_statemachine(finitestatemachines_StateMachine finitestatemachines_statemachine) {
        this.finitestatemachines_statemachine = finitestatemachines_statemachine;
    }
    public finitestatemachines_Trigger2 getFinitestatemachines_trigger2() {
        return finitestatemachines_trigger2;
    }

    public void setFinitestatemachines_trigger2(finitestatemachines_Trigger2 finitestatemachines_trigger2) {
        this.finitestatemachines_trigger2 = finitestatemachines_trigger2;
    }
    public finitestatemachines_StateMachine getFinitestatemachines_statemachine() {
        return finitestatemachines_statemachine;
    }

    public void setFinitestatemachines_statemachine(finitestatemachines_StateMachine finitestatemachines_statemachine) {
        this.finitestatemachines_statemachine = finitestatemachines_statemachine;
    }

}