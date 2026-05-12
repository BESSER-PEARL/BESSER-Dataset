





import java.util.List;
import java.util.ArrayList;

public class statemachine_GAbstractAction  {

    private String kind;





    private statemachine_GAbstractState statemachine_gabstractstate;


    public statemachine_GAbstractAction(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public statemachine_GAbstractState getStatemachine_gabstractstate() {
        return statemachine_gabstractstate;
    }

    public void setStatemachine_gabstractstate(statemachine_GAbstractState statemachine_gabstractstate) {
        this.statemachine_gabstractstate = statemachine_gabstractstate;
    }

}