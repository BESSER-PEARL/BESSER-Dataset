





import java.util.List;
import java.util.ArrayList;

public class junitresult_Testsuites extends AbstractAggregatedTest {

    private float time;
    private int disabled;



    public junitresult_Testsuites(
        float time,        int disabled    ) {
        super(
        );
        this.time = time;
        this.disabled = disabled;
    }


    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }
    public int getDisabled() {
        return disabled;
    }

    public void setDisabled(int disabled) {
        this.disabled = disabled;
    }


}