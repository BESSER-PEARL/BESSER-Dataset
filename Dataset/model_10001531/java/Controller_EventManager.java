





import java.util.List;
import java.util.ArrayList;

public class Controller_EventManager  {

    private boolean queueLock;
    private String eventQueue;





    private List<Controller_Event_union_> controller_event_union_s;




    private List<Controller_Controller> controller_controllers;


    public Controller_EventManager(
        boolean queueLock,        String eventQueue    ) {
        this.queueLock = queueLock;
        this.eventQueue = eventQueue;
        this.controller_event_union_s = new ArrayList<>();
        this.controller_controllers = new ArrayList<>();
    }

    public Controller_EventManager(
        boolean queueLock,        String eventQueue        ArrayList<Controller_Event_union_> controller_event_union_s,        ArrayList<Controller_Controller> controller_controllers    ) {
        this.queueLock = queueLock;
        this.eventQueue = eventQueue;
        this.controller_event_union_s = controller_event_union_s;
        this.controller_controllers = controller_controllers;
    }

    public boolean getQueuelock() {
        return queueLock;
    }

    public void setQueuelock(boolean queueLock) {
        this.queueLock = queueLock;
    }
    public String getEventqueue() {
        return eventQueue;
    }

    public void setEventqueue(String eventQueue) {
        this.eventQueue = eventQueue;
    }

    public List<Controller_Event_union_> getController_event_union_s() {
        return controller_event_union_s;
    }

    public void addController_event_union_(Controller_event_union_ controller_event_union_) {
        this.controller_event_union_s.add(controller_event_union_);
    }
    public List<Controller_Controller> getController_controllers() {
        return controller_controllers;
    }

    public void addController_controller(Controller_controller controller_controller) {
        this.controller_controllers.add(controller_controller);
    }

}