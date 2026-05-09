





import java.util.List;
import java.util.ArrayList;

public class rtsc_Clock extends NamedElement {

    private boolean uClock;





    private rtsc_ClockResetEvent rtsc_clockresetevent;


    public rtsc_Clock(
        boolean uClock    ) {
        super(
        );
        this.uClock = uClock;
    }


    public boolean getUclock() {
        return uClock;
    }

    public void setUclock(boolean uClock) {
        this.uClock = uClock;
    }

    public rtsc_ClockResetEvent getRtsc_clockresetevent() {
        return rtsc_clockresetevent;
    }

    public void setRtsc_clockresetevent(rtsc_ClockResetEvent rtsc_clockresetevent) {
        this.rtsc_clockresetevent = rtsc_clockresetevent;
    }

}