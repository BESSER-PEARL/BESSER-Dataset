





import java.util.List;
import java.util.ArrayList;

public class mindstorms_GoBackward extends Action {

    private boolean infinite;
    private int cm;



    public mindstorms_GoBackward(
        boolean infinite,        int cm    ) {
        super(
        );
        this.infinite = infinite;
        this.cm = cm;
    }


    public boolean getInfinite() {
        return infinite;
    }

    public void setInfinite(boolean infinite) {
        this.infinite = infinite;
    }
    public int getCm() {
        return cm;
    }

    public void setCm(int cm) {
        this.cm = cm;
    }


}