





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlTransitionType  {

    private String target;
    private String any;
    private String event;
    private String cond;
    private String scxmlExecutablecontent;





    private scxml_ScxmlStateType scxml_scxmlstatetype;




    private List<scxml_ScxmlScriptType> scxml_scxmlscripttypes;




    private List<scxml_ScxmlSendType> scxml_scxmlsendtypes;


    public scxml_ScxmlTransitionType(
        String target,        String any,        String event,        String cond,        String scxmlExecutablecontent    ) {
        this.target = target;
        this.any = any;
        this.event = event;
        this.cond = cond;
        this.scxmlExecutablecontent = scxmlExecutablecontent;
        this.scxml_scxmlscripttypes = new ArrayList<>();
        this.scxml_scxmlsendtypes = new ArrayList<>();
    }

    public scxml_ScxmlTransitionType(
        String target,        String any,        String event,        String cond,        String scxmlExecutablecontent        ArrayList<scxml_ScxmlScriptType> scxml_scxmlscripttypes,        ArrayList<scxml_ScxmlSendType> scxml_scxmlsendtypes    ) {
        this.target = target;
        this.any = any;
        this.event = event;
        this.cond = cond;
        this.scxmlExecutablecontent = scxmlExecutablecontent;
        this.scxml_scxmlscripttypes = scxml_scxmlscripttypes;
        this.scxml_scxmlsendtypes = scxml_scxmlsendtypes;
    }

    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
    }
    public String getScxmlexecutablecontent() {
        return scxmlExecutablecontent;
    }

    public void setScxmlexecutablecontent(String scxmlExecutablecontent) {
        this.scxmlExecutablecontent = scxmlExecutablecontent;
    }

    public scxml_ScxmlStateType getScxml_scxmlstatetype() {
        return scxml_scxmlstatetype;
    }

    public void setScxml_scxmlstatetype(scxml_ScxmlStateType scxml_scxmlstatetype) {
        this.scxml_scxmlstatetype = scxml_scxmlstatetype;
    }
    public List<scxml_ScxmlScriptType> getScxml_scxmlscripttypes() {
        return scxml_scxmlscripttypes;
    }

    public void addScxml_scxmlscripttype(Scxml_scxmlscripttype scxml_scxmlscripttype) {
        this.scxml_scxmlscripttypes.add(scxml_scxmlscripttype);
    }
    public List<scxml_ScxmlSendType> getScxml_scxmlsendtypes() {
        return scxml_scxmlsendtypes;
    }

    public void addScxml_scxmlsendtype(Scxml_scxmlsendtype scxml_scxmlsendtype) {
        this.scxml_scxmlsendtypes.add(scxml_scxmlsendtype);
    }

}