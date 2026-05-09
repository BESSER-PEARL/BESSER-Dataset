





import java.util.List;
import java.util.ArrayList;

public class finitestatemachines_State2 extends NamedElement {

    private int initialTime2;
    private int finalTime;





    private List<finitestatemachines_Transition2> finitestatemachines_transition2s;




    private finitestatemachines_StateMachine finitestatemachines_statemachine;




    private finitestatemachines_Transition2 finitestatemachines_transition2;




    private List<finitestatemachines_Transition2> finitestatemachines_transition2s;




    private finitestatemachines_Transition2 finitestatemachines_transition2;




    private finitestatemachines_StateMachine finitestatemachines_statemachine;


    public finitestatemachines_State2(
        int initialTime2,        int finalTime    ) {
        super(
        );
        this.initialTime2 = initialTime2;
        this.finalTime = finalTime;
        this.finitestatemachines_transition2s = new ArrayList<>();
        this.finitestatemachines_transition2s = new ArrayList<>();
    }

    public finitestatemachines_State2(
        int initialTime2,        int finalTime        ArrayList<finitestatemachines_Transition2> finitestatemachines_transition2s,        ArrayList<finitestatemachines_Transition2> finitestatemachines_transition2s    ) {
        this.initialTime2 = initialTime2;
        this.finalTime = finalTime;
        this.finitestatemachines_transition2s = finitestatemachines_transition2s;
        this.finitestatemachines_transition2s = finitestatemachines_transition2s;
    }

    public int getInitialtime2() {
        return initialTime2;
    }

    public void setInitialtime2(int initialTime2) {
        this.initialTime2 = initialTime2;
    }
    public int getFinaltime() {
        return finalTime;
    }

    public void setFinaltime(int finalTime) {
        this.finalTime = finalTime;
    }

    public List<finitestatemachines_Transition2> getFinitestatemachines_transition2s() {
        return finitestatemachines_transition2s;
    }

    public void addFinitestatemachines_transition2(Finitestatemachines_transition2 finitestatemachines_transition2) {
        this.finitestatemachines_transition2s.add(finitestatemachines_transition2);
    }
    public finitestatemachines_StateMachine getFinitestatemachines_statemachine() {
        return finitestatemachines_statemachine;
    }

    public void setFinitestatemachines_statemachine(finitestatemachines_StateMachine finitestatemachines_statemachine) {
        this.finitestatemachines_statemachine = finitestatemachines_statemachine;
    }
    public finitestatemachines_Transition2 getFinitestatemachines_transition2() {
        return finitestatemachines_transition2;
    }

    public void setFinitestatemachines_transition2(finitestatemachines_Transition2 finitestatemachines_transition2) {
        this.finitestatemachines_transition2 = finitestatemachines_transition2;
    }
    public List<finitestatemachines_Transition2> getFinitestatemachines_transition2s() {
        return finitestatemachines_transition2s;
    }

    public void addFinitestatemachines_transition2(Finitestatemachines_transition2 finitestatemachines_transition2) {
        this.finitestatemachines_transition2s.add(finitestatemachines_transition2);
    }
    public finitestatemachines_Transition2 getFinitestatemachines_transition2() {
        return finitestatemachines_transition2;
    }

    public void setFinitestatemachines_transition2(finitestatemachines_Transition2 finitestatemachines_transition2) {
        this.finitestatemachines_transition2 = finitestatemachines_transition2;
    }
    public finitestatemachines_StateMachine getFinitestatemachines_statemachine() {
        return finitestatemachines_statemachine;
    }

    public void setFinitestatemachines_statemachine(finitestatemachines_StateMachine finitestatemachines_statemachine) {
        this.finitestatemachines_statemachine = finitestatemachines_statemachine;
    }

}