





import java.util.List;
import java.util.ArrayList;

public class Event_Log  {

    private boolean Status;





    private Home_Security__Hub_ home_security__hub_;


    public Event_Log(
        boolean Status    ) {
        this.Status = Status;
    }


    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }

    public Home_Security__Hub_ getHome_security__hub_() {
        return home_security__hub_;
    }

    public void setHome_security__hub_(Home_Security__Hub_ home_security__hub_) {
        this.home_security__hub_ = home_security__hub_;
    }

}