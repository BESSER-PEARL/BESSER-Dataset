





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition extends NamedElement {

    private int time;
    private int initialTime;
    private int finalTime;



    public fsm_Transition(
        int time,        int initialTime,        int finalTime    ) {
        super(
        );
        this.time = time;
        this.initialTime = initialTime;
        this.finalTime = finalTime;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
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