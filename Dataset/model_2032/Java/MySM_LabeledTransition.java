





import java.util.List;
import java.util.ArrayList;

public class MySM_LabeledTransition extends Transition {






    private MySM_Action mysm_action;


    public MySM_LabeledTransition(
    ) {
        super(
        );
    }



    public MySM_Action getMysm_action() {
        return mysm_action;
    }

    public void setMysm_action(MySM_Action mysm_action) {
        this.mysm_action = mysm_action;
    }

}