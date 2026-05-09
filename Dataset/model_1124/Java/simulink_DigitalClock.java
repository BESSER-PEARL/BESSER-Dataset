





import java.util.List;
import java.util.ArrayList;

public class simulink_DigitalClock extends Block {

    private float sampleTime;



    public simulink_DigitalClock(
        float sampleTime    ) {
        super(
        );
        this.sampleTime = sampleTime;
    }


    public float getSampletime() {
        return sampleTime;
    }

    public void setSampletime(float sampleTime) {
        this.sampleTime = sampleTime;
    }


}