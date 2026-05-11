





import java.util.List;
import java.util.ArrayList;

public class krendering_KAction  {

    private String trigger;
    private boolean shiftPressed;
    private boolean altPressed;
    private boolean ctrlCmdPressed;
    private String actionId;



    public krendering_KAction(
        String trigger,        boolean shiftPressed,        boolean altPressed,        boolean ctrlCmdPressed,        String actionId    ) {
        this.trigger = trigger;
        this.shiftPressed = shiftPressed;
        this.altPressed = altPressed;
        this.ctrlCmdPressed = ctrlCmdPressed;
        this.actionId = actionId;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public boolean getShiftpressed() {
        return shiftPressed;
    }

    public void setShiftpressed(boolean shiftPressed) {
        this.shiftPressed = shiftPressed;
    }
    public boolean getAltpressed() {
        return altPressed;
    }

    public void setAltpressed(boolean altPressed) {
        this.altPressed = altPressed;
    }
    public boolean getCtrlcmdpressed() {
        return ctrlCmdPressed;
    }

    public void setCtrlcmdpressed(boolean ctrlCmdPressed) {
        this.ctrlCmdPressed = ctrlCmdPressed;
    }
    public String getActionid() {
        return actionId;
    }

    public void setActionid(String actionId) {
        this.actionId = actionId;
    }


}