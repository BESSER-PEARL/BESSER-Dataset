





import java.util.List;
import java.util.ArrayList;

public class Security_System  {

    private boolean systemOff;
    private boolean systemOn;



    public Security_System(
        boolean systemOff,        boolean systemOn    ) {
        this.systemOff = systemOff;
        this.systemOn = systemOn;
    }


    public boolean getSystemoff() {
        return systemOff;
    }

    public void setSystemoff(boolean systemOff) {
        this.systemOff = systemOff;
    }
    public boolean getSystemon() {
        return systemOn;
    }

    public void setSystemon(boolean systemOn) {
        this.systemOn = systemOn;
    }


}