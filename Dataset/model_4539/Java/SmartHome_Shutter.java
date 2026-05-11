





import java.util.List;
import java.util.ArrayList;

public class SmartHome_Shutter extends Activator {

    private boolean stateInit;



    public SmartHome_Shutter(
        boolean stateInit    ) {
        super(
        );
        this.stateInit = stateInit;
    }


    public boolean getStateinit() {
        return stateInit;
    }

    public void setStateinit(boolean stateInit) {
        this.stateInit = stateInit;
    }


}