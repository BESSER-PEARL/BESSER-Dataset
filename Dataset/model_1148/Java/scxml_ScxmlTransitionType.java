





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlTransitionType  {

    private String any;
    private String anyAttribute;
    private String cond;
    private String target;
    private String event;
    private String type;
    private String scxmlCoreExecutablecontent;





    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;




    private List<scxml_ScxmlLogType> scxml_scxmllogtypes;




    private scxml_ScxmlParallelType scxml_scxmlparalleltype;




    private List<scxml_ScxmlScriptType> scxml_scxmlscripttypes;




    private List<scxml_ScxmlRaiseType> scxml_scxmlraisetypes;




    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;




    private List<scxml_ScxmlSendType> scxml_scxmlsendtypes;




    private scxml_ScxmlInitialType scxml_scxmlinitialtype;




    private scxml_ScxmlStateType scxml_scxmlstatetype;




    private scxml_ScxmlHistoryType scxml_scxmlhistorytype;




    private List<scxml_ScxmlIfType> scxml_scxmliftypes;




    private List<scxml_ScxmlCancelType> scxml_scxmlcanceltypes;


    public scxml_ScxmlTransitionType(
        String any,        String anyAttribute,        String cond,        String target,        String event,        String type,        String scxmlCoreExecutablecontent    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.cond = cond;
        this.target = target;
        this.event = event;
        this.type = type;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlassigntypes = new ArrayList<>();
        this.scxml_scxmllogtypes = new ArrayList<>();
        this.scxml_scxmlscripttypes = new ArrayList<>();
        this.scxml_scxmlraisetypes = new ArrayList<>();
        this.scxml_scxmlforeachtypes = new ArrayList<>();
        this.scxml_scxmlsendtypes = new ArrayList<>();
        this.scxml_scxmliftypes = new ArrayList<>();
        this.scxml_scxmlcanceltypes = new ArrayList<>();
    }

    public scxml_ScxmlTransitionType(
        String any,        String anyAttribute,        String cond,        String target,        String event,        String type,        String scxmlCoreExecutablecontent        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes,        ArrayList<scxml_ScxmlLogType> scxml_scxmllogtypes,        ArrayList<scxml_ScxmlScriptType> scxml_scxmlscripttypes,        ArrayList<scxml_ScxmlRaiseType> scxml_scxmlraisetypes,        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes,        ArrayList<scxml_ScxmlSendType> scxml_scxmlsendtypes,        ArrayList<scxml_ScxmlIfType> scxml_scxmliftypes,        ArrayList<scxml_ScxmlCancelType> scxml_scxmlcanceltypes    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.cond = cond;
        this.target = target;
        this.event = event;
        this.type = type;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
        this.scxml_scxmllogtypes = scxml_scxmllogtypes;
        this.scxml_scxmlscripttypes = scxml_scxmlscripttypes;
        this.scxml_scxmlraisetypes = scxml_scxmlraisetypes;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
        this.scxml_scxmlsendtypes = scxml_scxmlsendtypes;
        this.scxml_scxmliftypes = scxml_scxmliftypes;
        this.scxml_scxmlcanceltypes = scxml_scxmlcanceltypes;
    }

    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getScxmlcoreexecutablecontent() {
        return scxmlCoreExecutablecontent;
    }

    public void setScxmlcoreexecutablecontent(String scxmlCoreExecutablecontent) {
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
    }

    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }
    public List<scxml_ScxmlLogType> getScxml_scxmllogtypes() {
        return scxml_scxmllogtypes;
    }

    public void addScxml_scxmllogtype(Scxml_scxmllogtype scxml_scxmllogtype) {
        this.scxml_scxmllogtypes.add(scxml_scxmllogtype);
    }
    public scxml_ScxmlParallelType getScxml_scxmlparalleltype() {
        return scxml_scxmlparalleltype;
    }

    public void setScxml_scxmlparalleltype(scxml_ScxmlParallelType scxml_scxmlparalleltype) {
        this.scxml_scxmlparalleltype = scxml_scxmlparalleltype;
    }
    public List<scxml_ScxmlScriptType> getScxml_scxmlscripttypes() {
        return scxml_scxmlscripttypes;
    }

    public void addScxml_scxmlscripttype(Scxml_scxmlscripttype scxml_scxmlscripttype) {
        this.scxml_scxmlscripttypes.add(scxml_scxmlscripttype);
    }
    public List<scxml_ScxmlRaiseType> getScxml_scxmlraisetypes() {
        return scxml_scxmlraisetypes;
    }

    public void addScxml_scxmlraisetype(Scxml_scxmlraisetype scxml_scxmlraisetype) {
        this.scxml_scxmlraisetypes.add(scxml_scxmlraisetype);
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }
    public List<scxml_ScxmlSendType> getScxml_scxmlsendtypes() {
        return scxml_scxmlsendtypes;
    }

    public void addScxml_scxmlsendtype(Scxml_scxmlsendtype scxml_scxmlsendtype) {
        this.scxml_scxmlsendtypes.add(scxml_scxmlsendtype);
    }
    public scxml_ScxmlInitialType getScxml_scxmlinitialtype() {
        return scxml_scxmlinitialtype;
    }

    public void setScxml_scxmlinitialtype(scxml_ScxmlInitialType scxml_scxmlinitialtype) {
        this.scxml_scxmlinitialtype = scxml_scxmlinitialtype;
    }
    public scxml_ScxmlStateType getScxml_scxmlstatetype() {
        return scxml_scxmlstatetype;
    }

    public void setScxml_scxmlstatetype(scxml_ScxmlStateType scxml_scxmlstatetype) {
        this.scxml_scxmlstatetype = scxml_scxmlstatetype;
    }
    public scxml_ScxmlHistoryType getScxml_scxmlhistorytype() {
        return scxml_scxmlhistorytype;
    }

    public void setScxml_scxmlhistorytype(scxml_ScxmlHistoryType scxml_scxmlhistorytype) {
        this.scxml_scxmlhistorytype = scxml_scxmlhistorytype;
    }
    public List<scxml_ScxmlIfType> getScxml_scxmliftypes() {
        return scxml_scxmliftypes;
    }

    public void addScxml_scxmliftype(Scxml_scxmliftype scxml_scxmliftype) {
        this.scxml_scxmliftypes.add(scxml_scxmliftype);
    }
    public List<scxml_ScxmlCancelType> getScxml_scxmlcanceltypes() {
        return scxml_scxmlcanceltypes;
    }

    public void addScxml_scxmlcanceltype(Scxml_scxmlcanceltype scxml_scxmlcanceltype) {
        this.scxml_scxmlcanceltypes.add(scxml_scxmlcanceltype);
    }

}