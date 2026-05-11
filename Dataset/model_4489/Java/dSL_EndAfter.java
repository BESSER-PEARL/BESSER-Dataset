





import java.util.List;
import java.util.ArrayList;

public class dSL_EndAfter extends EndCondition {

    private int time;



    public dSL_EndAfter(
        int time    ) {
        super(
        );
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }


}