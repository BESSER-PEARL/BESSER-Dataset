





import java.util.List;
import java.util.ArrayList;

public class arduinoml_AnalogAction extends Action {

    private int actionValue;



    public arduinoml_AnalogAction(
        int actionValue    ) {
        super(
        );
        this.actionValue = actionValue;
    }


    public int getActionvalue() {
        return actionValue;
    }

    public void setActionvalue(int actionValue) {
        this.actionValue = actionValue;
    }


}