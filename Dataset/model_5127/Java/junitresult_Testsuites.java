





import java.util.List;
import java.util.ArrayList;

public class junitresult_Testsuites extends AbstractAggregatedTest {

    private int disabled;
    private float time;



    public junitresult_Testsuites(
        int disabled,        float time    ) {
        super(
        );
        this.disabled = disabled;
        this.time = time;
    }


    public int getDisabled() {
        return disabled;
    }

    public void setDisabled(int disabled) {
        this.disabled = disabled;
    }
    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }


}