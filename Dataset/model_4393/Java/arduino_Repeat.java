





import java.util.List;
import java.util.ArrayList;

public class arduino_Repeat extends Control {

    private String iteration;



    public arduino_Repeat(
        String iteration    ) {
        super(
        );
        this.iteration = iteration;
    }


    public String getIteration() {
        return iteration;
    }

    public void setIteration(String iteration) {
        this.iteration = iteration;
    }


}