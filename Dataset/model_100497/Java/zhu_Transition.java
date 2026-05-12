





import java.util.List;
import java.util.ArrayList;

public class zhu_Transition  {

    private String guard;
    private String behaviour;



    public zhu_Transition(
        String guard,        String behaviour    ) {
        this.guard = guard;
        this.behaviour = behaviour;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getBehaviour() {
        return behaviour;
    }

    public void setBehaviour(String behaviour) {
        this.behaviour = behaviour;
    }


}