





import java.util.List;
import java.util.ArrayList;

public class occi_Action extends Category {






    private occi_Transition occi_transition;




    private occi_Type occi_type;


    public occi_Action(
    ) {
        super(
        );
    }



    public occi_Transition getOcci_transition() {
        return occi_transition;
    }

    public void setOcci_transition(occi_Transition occi_transition) {
        this.occi_transition = occi_transition;
    }
    public occi_Type getOcci_type() {
        return occi_type;
    }

    public void setOcci_type(occi_Type occi_type) {
        this.occi_type = occi_type;
    }

}