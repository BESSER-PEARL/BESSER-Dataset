





import java.util.List;
import java.util.ArrayList;

public class tfsm_Clock  {

    private int tick;
    private String name;





    private tfsm_TimedFSM tfsm_timedfsm;


    public tfsm_Clock(
        int tick,        String name    ) {
        this.tick = tick;
        this.name = name;
    }


    public int getTick() {
        return tick;
    }

    public void setTick(int tick) {
        this.tick = tick;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tfsm_TimedFSM getTfsm_timedfsm() {
        return tfsm_timedfsm;
    }

    public void setTfsm_timedfsm(tfsm_TimedFSM tfsm_timedfsm) {
        this.tfsm_timedfsm = tfsm_timedfsm;
    }

}