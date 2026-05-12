





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_TemporalGuard extends Guard {

    private int afterDuration;





    private ardurobotml_FSMClock ardurobotml_fsmclock;


    public ardurobotml_TemporalGuard(
        int afterDuration    ) {
        super(
        );
        this.afterDuration = afterDuration;
    }


    public int getAfterduration() {
        return afterDuration;
    }

    public void setAfterduration(int afterDuration) {
        this.afterDuration = afterDuration;
    }

    public ardurobotml_FSMClock getArdurobotml_fsmclock() {
        return ardurobotml_fsmclock;
    }

    public void setArdurobotml_fsmclock(ardurobotml_FSMClock ardurobotml_fsmclock) {
        this.ardurobotml_fsmclock = ardurobotml_fsmclock;
    }

}