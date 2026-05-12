





import java.util.List;
import java.util.ArrayList;

public class Controller_SDLInputController  {

    private None controllerPointer;
    private String eventList;



    public Controller_SDLInputController(
        None controllerPointer,        String eventList    ) {
        this.controllerPointer = controllerPointer;
        this.eventList = eventList;
    }


    public None getControllerpointer() {
        return controllerPointer;
    }

    public void setControllerpointer(None controllerPointer) {
        this.controllerPointer = controllerPointer;
    }
    public String getEventlist() {
        return eventList;
    }

    public void setEventlist(String eventList) {
        this.eventList = eventList;
    }


}