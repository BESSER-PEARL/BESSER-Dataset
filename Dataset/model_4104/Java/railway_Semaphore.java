





import java.util.List;
import java.util.ArrayList;

public class railway_Semaphore extends RailwayElement {

    private String signal;



    public railway_Semaphore(
        String signal    ) {
        super(
        );
        this.signal = signal;
    }


    public String getSignal() {
        return signal;
    }

    public void setSignal(String signal) {
        this.signal = signal;
    }


}