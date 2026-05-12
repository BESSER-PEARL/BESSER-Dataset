





import java.util.List;
import java.util.ArrayList;

public class tfsm_State extends NamedElement {

    private String OnEnterAction;



    public tfsm_State(
        String OnEnterAction    ) {
        super(
        );
        this.OnEnterAction = OnEnterAction;
    }


    public String getOnenteraction() {
        return OnEnterAction;
    }

    public void setOnenteraction(String OnEnterAction) {
        this.OnEnterAction = OnEnterAction;
    }


}