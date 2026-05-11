





import java.util.List;
import java.util.ArrayList;

public class dSL_Distance  {

    private int value;





    private dSL_Action dsl_action;




    private dSL_Condition dsl_condition;


    public dSL_Distance(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public dSL_Action getDsl_action() {
        return dsl_action;
    }

    public void setDsl_action(dSL_Action dsl_action) {
        this.dsl_action = dsl_action;
    }
    public dSL_Condition getDsl_condition() {
        return dsl_condition;
    }

    public void setDsl_condition(dSL_Condition dsl_condition) {
        this.dsl_condition = dsl_condition;
    }

}