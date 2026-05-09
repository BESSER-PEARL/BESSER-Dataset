





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_TemporalGuard extends Guard {

    private int afterDuration;





    private tfsmextended_FSMClock tfsmextended_fsmclock;


    public tfsmextended_TemporalGuard(
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

    public tfsmextended_FSMClock getTfsmextended_fsmclock() {
        return tfsmextended_fsmclock;
    }

    public void setTfsmextended_fsmclock(tfsmextended_FSMClock tfsmextended_fsmclock) {
        this.tfsmextended_fsmclock = tfsmextended_fsmclock;
    }

}