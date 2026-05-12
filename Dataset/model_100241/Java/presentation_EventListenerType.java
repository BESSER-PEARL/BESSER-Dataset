





import java.util.List;
import java.util.ArrayList;

public class presentation_EventListenerType  {

    private String type;
    private String actuate;
    private String effect;
    private String verb;
    private String speed;
    private String show;
    private String direction;
    private String action;
    private String eventName;
    private String href;
    private String startScale;





    private presentation_SoundType presentation_soundtype;


    public presentation_EventListenerType(
        String type,        String actuate,        String effect,        String verb,        String speed,        String show,        String direction,        String action,        String eventName,        String href,        String startScale    ) {
        this.type = type;
        this.actuate = actuate;
        this.effect = effect;
        this.verb = verb;
        this.speed = speed;
        this.show = show;
        this.direction = direction;
        this.action = action;
        this.eventName = eventName;
        this.href = href;
        this.startScale = startScale;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getActuate() {
        return actuate;
    }

    public void setActuate(String actuate) {
        this.actuate = actuate;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public String getVerb() {
        return verb;
    }

    public void setVerb(String verb) {
        this.verb = verb;
    }
    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getShow() {
        return show;
    }

    public void setShow(String show) {
        this.show = show;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getEventname() {
        return eventName;
    }

    public void setEventname(String eventName) {
        this.eventName = eventName;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getStartscale() {
        return startScale;
    }

    public void setStartscale(String startScale) {
        this.startScale = startScale;
    }

    public presentation_SoundType getPresentation_soundtype() {
        return presentation_soundtype;
    }

    public void setPresentation_soundtype(presentation_SoundType presentation_soundtype) {
        this.presentation_soundtype = presentation_soundtype;
    }

}