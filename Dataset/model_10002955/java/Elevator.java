





import java.util.List;
import java.util.ArrayList;

public class Elevator  {

    private None buttons;
    private None outOfServiceMech;
    private boolean isOutOfService;
    private None queue;
    private None emergencyButton;





    private ElevatorController elevatorcontroller;


    public Elevator(
        None buttons,        None outOfServiceMech,        boolean isOutOfService,        None queue,        None emergencyButton    ) {
        this.buttons = buttons;
        this.outOfServiceMech = outOfServiceMech;
        this.isOutOfService = isOutOfService;
        this.queue = queue;
        this.emergencyButton = emergencyButton;
    }


    public None getButtons() {
        return buttons;
    }

    public void setButtons(None buttons) {
        this.buttons = buttons;
    }
    public None getOutofservicemech() {
        return outOfServiceMech;
    }

    public void setOutofservicemech(None outOfServiceMech) {
        this.outOfServiceMech = outOfServiceMech;
    }
    public boolean getIsoutofservice() {
        return isOutOfService;
    }

    public void setIsoutofservice(boolean isOutOfService) {
        this.isOutOfService = isOutOfService;
    }
    public None getQueue() {
        return queue;
    }

    public void setQueue(None queue) {
        this.queue = queue;
    }
    public None getEmergencybutton() {
        return emergencyButton;
    }

    public void setEmergencybutton(None emergencyButton) {
        this.emergencyButton = emergencyButton;
    }

    public ElevatorController getElevatorcontroller() {
        return elevatorcontroller;
    }

    public void setElevatorcontroller(ElevatorController elevatorcontroller) {
        this.elevatorcontroller = elevatorcontroller;
    }

}