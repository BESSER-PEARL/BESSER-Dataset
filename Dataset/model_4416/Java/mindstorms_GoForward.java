





import java.util.List;
import java.util.ArrayList;

public class mindstorms_GoForward extends Action {

    private int cm;
    private boolean infinite;



    public mindstorms_GoForward(
        int cm,        boolean infinite    ) {
        super(
        );
        this.cm = cm;
        this.infinite = infinite;
    }


    public int getCm() {
        return cm;
    }

    public void setCm(int cm) {
        this.cm = cm;
    }
    public boolean getInfinite() {
        return infinite;
    }

    public void setInfinite(boolean infinite) {
        this.infinite = infinite;
    }


}