





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Wait extends Action {

    private int waitingTime;



    public arduinoml_Wait(
        int waitingTime    ) {
        super(
        );
        this.waitingTime = waitingTime;
    }


    public int getWaitingtime() {
        return waitingTime;
    }

    public void setWaitingtime(int waitingTime) {
        this.waitingTime = waitingTime;
    }


}