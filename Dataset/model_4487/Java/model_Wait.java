





import java.util.List;
import java.util.ArrayList;

public class model_Wait extends Command {

    private int time;



    public model_Wait(
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