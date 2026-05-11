





import java.util.List;
import java.util.ArrayList;

public class scxml_Send  {

    private String hintsexpr;
    private String targetexpr;
    private String eventexpr;
    private String delay;
    private String delayexpr;
    private String target;
    private String hints;
    private String idlocation;
    private String type;
    private String typeexpr;
    private String event;
    private String id;
    private String namelist;





    private scxml_If scxml_if;




    private List<scxml_Param> scxml_params;


    public scxml_Send(
        String hintsexpr,        String targetexpr,        String eventexpr,        String delay,        String delayexpr,        String target,        String hints,        String idlocation,        String type,        String typeexpr,        String event,        String id,        String namelist    ) {
        this.hintsexpr = hintsexpr;
        this.targetexpr = targetexpr;
        this.eventexpr = eventexpr;
        this.delay = delay;
        this.delayexpr = delayexpr;
        this.target = target;
        this.hints = hints;
        this.idlocation = idlocation;
        this.type = type;
        this.typeexpr = typeexpr;
        this.event = event;
        this.id = id;
        this.namelist = namelist;
        this.scxml_params = new ArrayList<>();
    }

    public scxml_Send(
        String hintsexpr,        String targetexpr,        String eventexpr,        String delay,        String delayexpr,        String target,        String hints,        String idlocation,        String type,        String typeexpr,        String event,        String id,        String namelist        ArrayList<scxml_Param> scxml_params    ) {
        this.hintsexpr = hintsexpr;
        this.targetexpr = targetexpr;
        this.eventexpr = eventexpr;
        this.delay = delay;
        this.delayexpr = delayexpr;
        this.target = target;
        this.hints = hints;
        this.idlocation = idlocation;
        this.type = type;
        this.typeexpr = typeexpr;
        this.event = event;
        this.id = id;
        this.namelist = namelist;
        this.scxml_params = scxml_params;
    }

    public String getHintsexpr() {
        return hintsexpr;
    }

    public void setHintsexpr(String hintsexpr) {
        this.hintsexpr = hintsexpr;
    }
    public String getTargetexpr() {
        return targetexpr;
    }

    public void setTargetexpr(String targetexpr) {
        this.targetexpr = targetexpr;
    }
    public String getEventexpr() {
        return eventexpr;
    }

    public void setEventexpr(String eventexpr) {
        this.eventexpr = eventexpr;
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
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getHints() {
        return hints;
    }

    public void setHints(String hints) {
        this.hints = hints;
    }
    public String getIdlocation() {
        return idlocation;
    }

    public void setIdlocation(String idlocation) {
        this.idlocation = idlocation;
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
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNamelist() {
        return namelist;
    }

    public void setNamelist(String namelist) {
        this.namelist = namelist;
    }

    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }
    public List<scxml_Param> getScxml_params() {
        return scxml_params;
    }

    public void addScxml_param(Scxml_param scxml_param) {
        this.scxml_params.add(scxml_param);
    }

}