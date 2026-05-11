





import java.util.List;
import java.util.ArrayList;

public class House2_Boiler extends Actor {

    private boolean isOn;



    public House2_Boiler(
        boolean isOn    ) {
        super(
        );
        this.isOn = isOn;
    }


    public boolean getIson() {
        return isOn;
    }

    public void setIson(boolean isOn) {
        this.isOn = isOn;
    }


}