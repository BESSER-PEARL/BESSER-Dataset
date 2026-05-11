





import java.util.List;
import java.util.ArrayList;

public class railway_Semaphore extends RailwayElement {

    private String signal;





    private railway_Segment railway_segment;


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

    public railway_Segment getRailway_segment() {
        return railway_segment;
    }

    public void setRailway_segment(railway_Segment railway_segment) {
        this.railway_segment = railway_segment;
    }

}