





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlSendType  {

    private String eventexpr;
    private String anyAttribute;
    private String typeexpr;
    private String targetexpr;
    private String namelist;
    private String delay;
    private String scxmlSendMix;
    private String event;
    private String id;
    private String type;
    private String idlocation;
    private String any;
    private String delayexpr;
    private String target;





    private scxml_ScxmlOnexitType scxml_scxmlonexittype;




    private scxml_ScxmlOnentryType scxml_scxmlonentrytype;




    private List<scxml_ScxmlContentType> scxml_scxmlcontenttypes;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private scxml_DocumentRoot scxml_documentroot;




    private scxml_ScxmlForeachType scxml_scxmlforeachtype;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private List<scxml_ScxmlParamType> scxml_scxmlparamtypes;




    private scxml_ScxmlFinalizeType scxml_scxmlfinalizetype;




    private scxml_ScxmlIfType scxml_scxmliftype;


    public scxml_ScxmlSendType(
        String eventexpr,        String anyAttribute,        String typeexpr,        String targetexpr,        String namelist,        String delay,        String scxmlSendMix,        String event,        String id,        String type,        String idlocation,        String any,        String delayexpr,        String target    ) {
        this.eventexpr = eventexpr;
        this.anyAttribute = anyAttribute;
        this.typeexpr = typeexpr;
        this.targetexpr = targetexpr;
        this.namelist = namelist;
        this.delay = delay;
        this.scxmlSendMix = scxmlSendMix;
        this.event = event;
        this.id = id;
        this.type = type;
        this.idlocation = idlocation;
        this.any = any;
        this.delayexpr = delayexpr;
        this.target = target;
        this.scxml_scxmlcontenttypes = new ArrayList<>();
        this.scxml_scxmlparamtypes = new ArrayList<>();
    }

    public scxml_ScxmlSendType(
        String eventexpr,        String anyAttribute,        String typeexpr,        String targetexpr,        String namelist,        String delay,        String scxmlSendMix,        String event,        String id,        String type,        String idlocation,        String any,        String delayexpr,        String target        ArrayList<scxml_ScxmlContentType> scxml_scxmlcontenttypes,        ArrayList<scxml_ScxmlParamType> scxml_scxmlparamtypes    ) {
        this.eventexpr = eventexpr;
        this.anyAttribute = anyAttribute;
        this.typeexpr = typeexpr;
        this.targetexpr = targetexpr;
        this.namelist = namelist;
        this.delay = delay;
        this.scxmlSendMix = scxmlSendMix;
        this.event = event;
        this.id = id;
        this.type = type;
        this.idlocation = idlocation;
        this.any = any;
        this.delayexpr = delayexpr;
        this.target = target;
        this.scxml_scxmlcontenttypes = scxml_scxmlcontenttypes;
        this.scxml_scxmlparamtypes = scxml_scxmlparamtypes;
    }

    public String getEventexpr() {
        return eventexpr;
    }

    public void setEventexpr(String eventexpr) {
        this.eventexpr = eventexpr;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getTypeexpr() {
        return typeexpr;
    }

    public void setTypeexpr(String typeexpr) {
        this.typeexpr = typeexpr;
    }
    public String getTargetexpr() {
        return targetexpr;
    }

    public void setTargetexpr(String targetexpr) {
        this.targetexpr = targetexpr;
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
    public String getScxmlsendmix() {
        return scxmlSendMix;
    }

    public void setScxmlsendmix(String scxmlSendMix) {
        this.scxmlSendMix = scxmlSendMix;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIdlocation() {
        return idlocation;
    }

    public void setIdlocation(String idlocation) {
        this.idlocation = idlocation;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
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

    public scxml_ScxmlOnexitType getScxml_scxmlonexittype() {
        return scxml_scxmlonexittype;
    }

    public void setScxml_scxmlonexittype(scxml_ScxmlOnexitType scxml_scxmlonexittype) {
        this.scxml_scxmlonexittype = scxml_scxmlonexittype;
    }
    public scxml_ScxmlOnentryType getScxml_scxmlonentrytype() {
        return scxml_scxmlonentrytype;
    }

    public void setScxml_scxmlonentrytype(scxml_ScxmlOnentryType scxml_scxmlonentrytype) {
        this.scxml_scxmlonentrytype = scxml_scxmlonentrytype;
    }
    public List<scxml_ScxmlContentType> getScxml_scxmlcontenttypes() {
        return scxml_scxmlcontenttypes;
    }

    public void addScxml_scxmlcontenttype(Scxml_scxmlcontenttype scxml_scxmlcontenttype) {
        this.scxml_scxmlcontenttypes.add(scxml_scxmlcontenttype);
    }
    public scxml_ScxmlIfType getScxml_scxmliftype() {
        return scxml_scxmliftype;
    }

    public void setScxml_scxmliftype(scxml_ScxmlIfType scxml_scxmliftype) {
        this.scxml_scxmliftype = scxml_scxmliftype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public scxml_ScxmlForeachType getScxml_scxmlforeachtype() {
        return scxml_scxmlforeachtype;
    }

    public void setScxml_scxmlforeachtype(scxml_ScxmlForeachType scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtype = scxml_scxmlforeachtype;
    }
    public scxml_ScxmlIfType getScxml_scxmliftype() {
        return scxml_scxmliftype;
    }

    public void setScxml_scxmliftype(scxml_ScxmlIfType scxml_scxmliftype) {
        this.scxml_scxmliftype = scxml_scxmliftype;
    }
    public List<scxml_ScxmlParamType> getScxml_scxmlparamtypes() {
        return scxml_scxmlparamtypes;
    }

    public void addScxml_scxmlparamtype(Scxml_scxmlparamtype scxml_scxmlparamtype) {
        this.scxml_scxmlparamtypes.add(scxml_scxmlparamtype);
    }
    public scxml_ScxmlFinalizeType getScxml_scxmlfinalizetype() {
        return scxml_scxmlfinalizetype;
    }

    public void setScxml_scxmlfinalizetype(scxml_ScxmlFinalizeType scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetype = scxml_scxmlfinalizetype;
    }
    public scxml_ScxmlIfType getScxml_scxmliftype() {
        return scxml_scxmliftype;
    }

    public void setScxml_scxmliftype(scxml_ScxmlIfType scxml_scxmliftype) {
        this.scxml_scxmliftype = scxml_scxmliftype;
    }

}