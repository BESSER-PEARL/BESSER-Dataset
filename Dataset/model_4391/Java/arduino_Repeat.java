





import java.util.List;
import java.util.ArrayList;

public class arduino_Repeat extends Control {

    private int iteration;



    public arduino_Repeat(
        int iteration    ) {
        super(
        );
        this.iteration = iteration;
    }


    public int getIteration() {
        return iteration;
    }

    public void setIteration(int iteration) {
        this.iteration = iteration;
    }


}