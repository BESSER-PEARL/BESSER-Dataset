





import java.util.List;
import java.util.ArrayList;

public class farrusco_LED extends Actuate {

    private boolean on_off;



    public farrusco_LED(
        boolean on_off    ) {
        super(
        );
        this.on_off = on_off;
    }


    public boolean getOn_off() {
        return on_off;
    }

    public void setOn_off(boolean on_off) {
        this.on_off = on_off;
    }


}