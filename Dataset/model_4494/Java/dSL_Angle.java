





import java.util.List;
import java.util.ArrayList;

public class dSL_Angle  {

    private int value;
    private boolean away;





    private dSL_Action dsl_action;


    public dSL_Angle(
        int value,        boolean away    ) {
        this.value = value;
        this.away = away;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public boolean getAway() {
        return away;
    }

    public void setAway(boolean away) {
        this.away = away;
    }

    public dSL_Action getDsl_action() {
        return dsl_action;
    }

    public void setDsl_action(dSL_Action dsl_action) {
        this.dsl_action = dsl_action;
    }

}