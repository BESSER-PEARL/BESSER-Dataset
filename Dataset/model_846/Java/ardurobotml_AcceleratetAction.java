





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_AcceleratetAction extends Action {

    private int startTick;
    private int ratio;



    public ardurobotml_AcceleratetAction(
        int startTick,        int ratio    ) {
        super(
        );
        this.startTick = startTick;
        this.ratio = ratio;
    }


    public int getStarttick() {
        return startTick;
    }

    public void setStarttick(int startTick) {
        this.startTick = startTick;
    }
    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }


}