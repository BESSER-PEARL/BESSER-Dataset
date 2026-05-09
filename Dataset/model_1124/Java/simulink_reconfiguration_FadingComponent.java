





import java.util.List;
import java.util.ArrayList;

public class simulink_reconfiguration_FadingComponent extends Block {

    private int time;



    public simulink_reconfiguration_FadingComponent(
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