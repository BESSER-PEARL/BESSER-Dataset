





import java.util.List;
import java.util.ArrayList;

public class krendering_KAction  {

    private String altPressed;
    private String actionId;
    private String shiftPressed;
    private String trigger;
    private String ctrlCmdPressed;





    private krendering_KRendering krendering_krendering;


    public krendering_KAction(
        String altPressed,        String actionId,        String shiftPressed,        String trigger,        String ctrlCmdPressed    ) {
        this.altPressed = altPressed;
        this.actionId = actionId;
        this.shiftPressed = shiftPressed;
        this.trigger = trigger;
        this.ctrlCmdPressed = ctrlCmdPressed;
    }


    public String getAltpressed() {
        return altPressed;
    }

    public void setAltpressed(String altPressed) {
        this.altPressed = altPressed;
    }
    public String getActionid() {
        return actionId;
    }

    public void setActionid(String actionId) {
        this.actionId = actionId;
    }
    public String getShiftpressed() {
        return shiftPressed;
    }

    public void setShiftpressed(String shiftPressed) {
        this.shiftPressed = shiftPressed;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getCtrlcmdpressed() {
        return ctrlCmdPressed;
    }

    public void setCtrlcmdpressed(String ctrlCmdPressed) {
        this.ctrlCmdPressed = ctrlCmdPressed;
    }

    public krendering_KRendering getKrendering_krendering() {
        return krendering_krendering;
    }

    public void setKrendering_krendering(krendering_KRendering krendering_krendering) {
        this.krendering_krendering = krendering_krendering;
    }

}