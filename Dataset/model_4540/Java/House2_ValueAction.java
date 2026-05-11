





import java.util.List;
import java.util.ArrayList;

public class House2_ValueAction extends Action {

    private float switchToValue;



    public House2_ValueAction(
        float switchToValue    ) {
        super(
        );
        this.switchToValue = switchToValue;
    }


    public float getSwitchtovalue() {
        return switchToValue;
    }

    public void setSwitchtovalue(float switchToValue) {
        this.switchToValue = switchToValue;
    }


}