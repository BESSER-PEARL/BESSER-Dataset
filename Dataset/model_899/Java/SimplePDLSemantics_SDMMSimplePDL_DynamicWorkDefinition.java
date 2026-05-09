





import java.util.List;
import java.util.ArrayList;

public class SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition extends WorkDefinition {

    private String time;
    private String state;
    private float timeElapsed;



    public SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition(
        String time,        String state,        float timeElapsed    ) {
        super(
        );
        this.time = time;
        this.state = state;
        this.timeElapsed = timeElapsed;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public float getTimeelapsed() {
        return timeElapsed;
    }

    public void setTimeelapsed(float timeElapsed) {
        this.timeElapsed = timeElapsed;
    }


}