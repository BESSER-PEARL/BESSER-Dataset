





import java.util.List;
import java.util.ArrayList;

public class arduino_Repeat extends Control {

    private String i;
    private int iteration;



    public arduino_Repeat(
        String i,        int iteration    ) {
        super(
        );
        this.i = i;
        this.iteration = iteration;
    }


    public String getI() {
        return i;
    }

    public void setI(String i) {
        this.i = i;
    }
    public int getIteration() {
        return iteration;
    }

    public void setIteration(int iteration) {
        this.iteration = iteration;
    }


}