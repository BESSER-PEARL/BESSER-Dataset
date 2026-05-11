





import java.util.List;
import java.util.ArrayList;

public class farrusco_Wait extends Condition {

    private int time;



    public farrusco_Wait(
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