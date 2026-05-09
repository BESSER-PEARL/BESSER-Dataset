





import java.util.List;
import java.util.ArrayList;

public class rtsc_Clock extends NamedElement {

    private boolean uClock;



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


}