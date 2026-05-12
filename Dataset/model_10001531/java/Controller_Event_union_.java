





import java.util.List;
import java.util.ArrayList;

public class Controller_Event_union_  {

    private String EventMouseButton;
    private String EventMouseWheel;
    private String eventType;
    private String EventEmpty;
    private String EventMouseMotion;
    private String EvenkKeyboard;
    private String EventQuit;



    public Controller_Event_union_(
        String EventMouseButton,        String EventMouseWheel,        String eventType,        String EventEmpty,        String EventMouseMotion,        String EvenkKeyboard,        String EventQuit    ) {
        this.EventMouseButton = EventMouseButton;
        this.EventMouseWheel = EventMouseWheel;
        this.eventType = eventType;
        this.EventEmpty = EventEmpty;
        this.EventMouseMotion = EventMouseMotion;
        this.EvenkKeyboard = EvenkKeyboard;
        this.EventQuit = EventQuit;
    }


    public String getEventmousebutton() {
        return EventMouseButton;
    }

    public void setEventmousebutton(String EventMouseButton) {
        this.EventMouseButton = EventMouseButton;
    }
    public String getEventmousewheel() {
        return EventMouseWheel;
    }

    public void setEventmousewheel(String EventMouseWheel) {
        this.EventMouseWheel = EventMouseWheel;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getEventempty() {
        return EventEmpty;
    }

    public void setEventempty(String EventEmpty) {
        this.EventEmpty = EventEmpty;
    }
    public String getEventmousemotion() {
        return EventMouseMotion;
    }

    public void setEventmousemotion(String EventMouseMotion) {
        this.EventMouseMotion = EventMouseMotion;
    }
    public String getEvenkkeyboard() {
        return EvenkKeyboard;
    }

    public void setEvenkkeyboard(String EvenkKeyboard) {
        this.EvenkKeyboard = EvenkKeyboard;
    }
    public String getEventquit() {
        return EventQuit;
    }

    public void setEventquit(String EventQuit) {
        this.EventQuit = EventQuit;
    }


}