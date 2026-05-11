





import java.util.List;
import java.util.ArrayList;

public class wsn_TimingAction extends Action,  {

    private int time;



    public wsn_TimingAction(
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