





import java.util.List;
import java.util.ArrayList;

public class behaviour_FieldObject  {






    private behaviour_Condition behaviour_condition;




    private behaviour_MoveTo behaviour_moveto;




    private behaviour_PerformAction behaviour_performaction;


    public behaviour_FieldObject(
    ) {
    }



    public behaviour_Condition getBehaviour_condition() {
        return behaviour_condition;
    }

    public void setBehaviour_condition(behaviour_Condition behaviour_condition) {
        this.behaviour_condition = behaviour_condition;
    }
    public behaviour_MoveTo getBehaviour_moveto() {
        return behaviour_moveto;
    }

    public void setBehaviour_moveto(behaviour_MoveTo behaviour_moveto) {
        this.behaviour_moveto = behaviour_moveto;
    }
    public behaviour_PerformAction getBehaviour_performaction() {
        return behaviour_performaction;
    }

    public void setBehaviour_performaction(behaviour_PerformAction behaviour_performaction) {
        this.behaviour_performaction = behaviour_performaction;
    }

}