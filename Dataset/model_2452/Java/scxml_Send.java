





import java.util.List;
import java.util.ArrayList;

public class scxml_Send extends Donedata {

    private String namelist;
    private String delay;
    private String delayexpr;
    private String hints;
    private String type;
    private String typeexpr;
    private String hintsexpr;
    private String id;
    private String targetexpr;
    private String target;
    private String event;
    private String eventexpr;
    private String idlocation;





    private scxml_ExecutableContent scxml_executablecontent;


    public scxml_Send(
        String namelist,        String delay,        String delayexpr,        String hints,        String type,        String typeexpr,        String hintsexpr,        String id,        String targetexpr,        String target,        String event,        String eventexpr,        String idlocation    ) {
        super(
        );
        this.namelist = namelist;
        this.delay = delay;
        this.delayexpr = delayexpr;
        this.hints = hints;
        this.type = type;
        this.typeexpr = typeexpr;
        this.hintsexpr = hintsexpr;
        this.id = id;
        this.targetexpr = targetexpr;
        this.target = target;
        this.event = event;
        this.eventexpr = eventexpr;
        this.idlocation = idlocation;
    }


    public String getNamelist() {
        return namelist;
    }

    public void setNamelist(String namelist) {
        this.namelist = namelist;
    }
    public String getDelay() {
        return delay;
    }

    public void setDelay(String delay) {
        this.delay = delay;
    }
    public String getDelayexpr() {
        return delayexpr;
    }

    public void setDelayexpr(String delayexpr) {
        this.delayexpr = delayexpr;
    }
    public String getHints() {
        return hints;
    }

    public void setHints(String hints) {
        this.hints = hints;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTypeexpr() {
        return typeexpr;
    }

    public void setTypeexpr(String typeexpr) {
        this.typeexpr = typeexpr;
    }
    public String getHintsexpr() {
        return hintsexpr;
    }

    public void setHintsexpr(String hintsexpr) {
        this.hintsexpr = hintsexpr;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTargetexpr() {
        return targetexpr;
    }

    public void setTargetexpr(String targetexpr) {
        this.targetexpr = targetexpr;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getEventexpr() {
        return eventexpr;
    }

    public void setEventexpr(String eventexpr) {
        this.eventexpr = eventexpr;
    }
    public String getIdlocation() {
        return idlocation;
    }

    public void setIdlocation(String idlocation) {
        this.idlocation = idlocation;
    }

    public scxml_ExecutableContent getScxml_executablecontent() {
        return scxml_executablecontent;
    }

    public void setScxml_executablecontent(scxml_ExecutableContent scxml_executablecontent) {
        this.scxml_executablecontent = scxml_executablecontent;
    }

}