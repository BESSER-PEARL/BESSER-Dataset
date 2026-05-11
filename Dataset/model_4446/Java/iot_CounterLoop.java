





import java.util.List;
import java.util.ArrayList;

public class iot_CounterLoop extends Iteration {

    private int counter;



    public iot_CounterLoop(
        int counter    ) {
        super(
        );
        this.counter = counter;
    }


    public int getCounter() {
        return counter;
    }

    public void setCounter(int counter) {
        this.counter = counter;
    }


}