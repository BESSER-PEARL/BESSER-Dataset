





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition extends NamedElement {

    private int initialTime;
    private int finalTime;



    public fsm_Transition(
        int initialTime,        int finalTime    ) {
        super(
        );
        this.initialTime = initialTime;
        this.finalTime = finalTime;
    }


    public int getInitialtime() {
        return initialTime;
    }

    public void setInitialtime(int initialTime) {
        this.initialTime = initialTime;
    }
    public int getFinaltime() {
        return finalTime;
    }

    public void setFinaltime(int finalTime) {
        this.finalTime = finalTime;
    }


}