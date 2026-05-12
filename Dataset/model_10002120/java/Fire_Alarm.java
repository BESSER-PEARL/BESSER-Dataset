





import java.util.List;
import java.util.ArrayList;

public class Fire_Alarm  {

    private boolean systemOn;
    private boolean systemOff;



    public Fire_Alarm(
        boolean systemOn,        boolean systemOff    ) {
        this.systemOn = systemOn;
        this.systemOff = systemOff;
    }


    public boolean getSystemon() {
        return systemOn;
    }

    public void setSystemon(boolean systemOn) {
        this.systemOn = systemOn;
    }
    public boolean getSystemoff() {
        return systemOff;
    }

    public void setSystemoff(boolean systemOff) {
        this.systemOff = systemOff;
    }


}