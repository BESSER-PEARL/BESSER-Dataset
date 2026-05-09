





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_DeceleratetAction extends Action {

    private int ratio;
    private int startTick;



    public ardurobotml_DeceleratetAction(
        int ratio,        int startTick    ) {
        super(
        );
        this.ratio = ratio;
        this.startTick = startTick;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }
    public int getStarttick() {
        return startTick;
    }

    public void setStarttick(int startTick) {
        this.startTick = startTick;
    }


}