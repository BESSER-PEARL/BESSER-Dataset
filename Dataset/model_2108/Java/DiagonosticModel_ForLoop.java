





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_ForLoop extends BlockAction {

    private int startValue;
    private String loopVar;
    private int stopValue;



    public DiagonosticModel_ForLoop(
        int startValue,        String loopVar,        int stopValue    ) {
        super(
        );
        this.startValue = startValue;
        this.loopVar = loopVar;
        this.stopValue = stopValue;
    }


    public int getStartvalue() {
        return startValue;
    }

    public void setStartvalue(int startValue) {
        this.startValue = startValue;
    }
    public String getLoopvar() {
        return loopVar;
    }

    public void setLoopvar(String loopVar) {
        this.loopVar = loopVar;
    }
    public int getStopvalue() {
        return stopValue;
    }

    public void setStopvalue(int stopValue) {
        this.stopValue = stopValue;
    }


}