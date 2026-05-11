





import java.util.List;
import java.util.ArrayList;

public class arduino_Precondition  {

    private String op;





    private arduino_Precondition arduino_precondition;




    private arduino_LoopItem arduino_loopitem;


    public arduino_Precondition(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public arduino_Precondition getArduino_precondition() {
        return arduino_precondition;
    }

    public void setArduino_precondition(arduino_Precondition arduino_precondition) {
        this.arduino_precondition = arduino_precondition;
    }
    public arduino_LoopItem getArduino_loopitem() {
        return arduino_loopitem;
    }

    public void setArduino_loopitem(arduino_LoopItem arduino_loopitem) {
        this.arduino_loopitem = arduino_loopitem;
    }

}