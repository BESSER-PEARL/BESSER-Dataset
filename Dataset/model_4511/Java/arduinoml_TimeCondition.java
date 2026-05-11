





import java.util.List;
import java.util.ArrayList;

public class arduinoml_TimeCondition extends Condition {

    private int time;
    private String tComp;



    public arduinoml_TimeCondition(
        int time,        String tComp    ) {
        super(
        );
        this.time = time;
        this.tComp = tComp;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getTcomp() {
        return tComp;
    }

    public void setTcomp(String tComp) {
        this.tComp = tComp;
    }


}