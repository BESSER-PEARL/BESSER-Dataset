





import java.util.List;
import java.util.ArrayList;

public class arduino_Repeat extends Control {

    private int iteration;
    private String i;



    public arduino_Repeat(
        int iteration,        String i    ) {
        super(
        );
        this.iteration = iteration;
        this.i = i;
    }


    public int getIteration() {
        return iteration;
    }

    public void setIteration(int iteration) {
        this.iteration = iteration;
    }
    public String getI() {
        return i;
    }

    public void setI(String i) {
        this.i = i;
    }


}