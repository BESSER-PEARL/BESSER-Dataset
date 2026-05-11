





import java.util.List;
import java.util.ArrayList;

public class dSL_MovementAction  {

    private String actionenum;





    private dSL_RightMovementAction dsl_rightmovementaction;




    private dSL_LeftMovementAction dsl_leftmovementaction;


    public dSL_MovementAction(
        String actionenum    ) {
        this.actionenum = actionenum;
    }


    public String getActionenum() {
        return actionenum;
    }

    public void setActionenum(String actionenum) {
        this.actionenum = actionenum;
    }

    public dSL_RightMovementAction getDsl_rightmovementaction() {
        return dsl_rightmovementaction;
    }

    public void setDsl_rightmovementaction(dSL_RightMovementAction dsl_rightmovementaction) {
        this.dsl_rightmovementaction = dsl_rightmovementaction;
    }
    public dSL_LeftMovementAction getDsl_leftmovementaction() {
        return dsl_leftmovementaction;
    }

    public void setDsl_leftmovementaction(dSL_LeftMovementAction dsl_leftmovementaction) {
        this.dsl_leftmovementaction = dsl_leftmovementaction;
    }

}