





import java.util.List;
import java.util.ArrayList;

public class simulink_ZeroOrderHold extends Block {

    private String sampleTime;



    public simulink_ZeroOrderHold(
        String sampleTime    ) {
        super(
        );
        this.sampleTime = sampleTime;
    }


    public String getSampletime() {
        return sampleTime;
    }

    public void setSampletime(String sampleTime) {
        this.sampleTime = sampleTime;
    }


}