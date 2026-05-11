





import java.util.List;
import java.util.ArrayList;

public class robochart_Connection  {

    private boolean bidirec;
    private boolean async_;





    private robochart_Event robochart_event;




    private robochart_RCModule robochart_rcmodule;




    private robochart_Event robochart_event;




    private robochart_ControllerDef robochart_controllerdef;


    public robochart_Connection(
        boolean bidirec,        boolean async_    ) {
        this.bidirec = bidirec;
        this.async_ = async_;
    }


    public boolean getBidirec() {
        return bidirec;
    }

    public void setBidirec(boolean bidirec) {
        this.bidirec = bidirec;
    }
    public boolean getAsync_() {
        return async_;
    }

    public void setAsync_(boolean async_) {
        this.async_ = async_;
    }

    public robochart_Event getRobochart_event() {
        return robochart_event;
    }

    public void setRobochart_event(robochart_Event robochart_event) {
        this.robochart_event = robochart_event;
    }
    public robochart_RCModule getRobochart_rcmodule() {
        return robochart_rcmodule;
    }

    public void setRobochart_rcmodule(robochart_RCModule robochart_rcmodule) {
        this.robochart_rcmodule = robochart_rcmodule;
    }
    public robochart_Event getRobochart_event() {
        return robochart_event;
    }

    public void setRobochart_event(robochart_Event robochart_event) {
        this.robochart_event = robochart_event;
    }
    public robochart_ControllerDef getRobochart_controllerdef() {
        return robochart_controllerdef;
    }

    public void setRobochart_controllerdef(robochart_ControllerDef robochart_controllerdef) {
        this.robochart_controllerdef = robochart_controllerdef;
    }

}