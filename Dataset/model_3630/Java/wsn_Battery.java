





import java.util.List;
import java.util.ArrayList;

public class wsn_Battery extends , EnergySource {

    private float empty;
    private float full;



    public wsn_Battery(
        float empty,        float full    ) {
        super(
        );
        this.empty = empty;
        this.full = full;
    }


    public float getEmpty() {
        return empty;
    }

    public void setEmpty(float empty) {
        this.empty = empty;
    }
    public float getFull() {
        return full;
    }

    public void setFull(float full) {
        this.full = full;
    }


}