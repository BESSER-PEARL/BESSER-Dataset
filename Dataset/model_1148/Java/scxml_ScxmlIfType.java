





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlIfType  {

    private String any1;
    private String any2;
    private String cond;
    private String anyAttribute;
    private String any;
    private String scxmlCoreExecutablecontent1;
    private String scxmlCoreExecutablecontent;
    private String scxmlCoreExecutablecontent2;





    private scxml_ScxmlFinalizeType scxml_scxmlfinalizetype;




    private List<scxml_ScxmlRaiseType> scxml_scxmlraisetypes;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;




    private List<scxml_ScxmlCancelType> scxml_scxmlcanceltypes;




    private scxml_ScxmlElseType scxml_scxmlelsetype;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private List<scxml_ScxmlRaiseType> scxml_scxmlraisetypes;




    private scxml_ScxmlOnexitType scxml_scxmlonexittype;




    private List<scxml_ScxmlRaiseType> scxml_scxmlraisetypes;




    private List<scxml_ScxmlIfType> scxml_scxmliftypes;




    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;




    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;




    private List<scxml_ScxmlCancelType> scxml_scxmlcanceltypes;




    private scxml_ScxmlElseifType scxml_scxmlelseiftype;




    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;




    private List<scxml_ScxmlCancelType> scxml_scxmlcanceltypes;




    private scxml_ScxmlForeachType scxml_scxmlforeachtype;




    private scxml_ScxmlOnentryType scxml_scxmlonentrytype;




    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlIfType(
        String any1,        String any2,        String cond,        String anyAttribute,        String any,        String scxmlCoreExecutablecontent1,        String scxmlCoreExecutablecontent,        String scxmlCoreExecutablecontent2    ) {
        this.any1 = any1;
        this.any2 = any2;
        this.cond = cond;
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.scxmlCoreExecutablecontent1 = scxmlCoreExecutablecontent1;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxmlCoreExecutablecontent2 = scxmlCoreExecutablecontent2;
        this.scxml_scxmlraisetypes = new ArrayList<>();
        this.scxml_scxmlassigntypes = new ArrayList<>();
        this.scxml_scxmlcanceltypes = new ArrayList<>();
        this.scxml_scxmlassigntypes = new ArrayList<>();
        this.scxml_scxmlraisetypes = new ArrayList<>();
        this.scxml_scxmlraisetypes = new ArrayList<>();
        this.scxml_scxmliftypes = new ArrayList<>();
        this.scxml_scxmlforeachtypes = new ArrayList<>();
        this.scxml_scxmlforeachtypes = new ArrayList<>();
        this.scxml_scxmlassigntypes = new ArrayList<>();
        this.scxml_scxmlcanceltypes = new ArrayList<>();
        this.scxml_scxmlforeachtypes = new ArrayList<>();
        this.scxml_scxmlcanceltypes = new ArrayList<>();
    }

    public scxml_ScxmlIfType(
        String any1,        String any2,        String cond,        String anyAttribute,        String any,        String scxmlCoreExecutablecontent1,        String scxmlCoreExecutablecontent,        String scxmlCoreExecutablecontent2        ArrayList<scxml_ScxmlRaiseType> scxml_scxmlraisetypes,        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes,        ArrayList<scxml_ScxmlCancelType> scxml_scxmlcanceltypes,        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes,        ArrayList<scxml_ScxmlRaiseType> scxml_scxmlraisetypes,        ArrayList<scxml_ScxmlRaiseType> scxml_scxmlraisetypes,        ArrayList<scxml_ScxmlIfType> scxml_scxmliftypes,        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes,        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes,        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes,        ArrayList<scxml_ScxmlCancelType> scxml_scxmlcanceltypes,        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes,        ArrayList<scxml_ScxmlCancelType> scxml_scxmlcanceltypes    ) {
        this.any1 = any1;
        this.any2 = any2;
        this.cond = cond;
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.scxmlCoreExecutablecontent1 = scxmlCoreExecutablecontent1;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxmlCoreExecutablecontent2 = scxmlCoreExecutablecontent2;
        this.scxml_scxmlraisetypes = scxml_scxmlraisetypes;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
        this.scxml_scxmlcanceltypes = scxml_scxmlcanceltypes;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
        this.scxml_scxmlraisetypes = scxml_scxmlraisetypes;
        this.scxml_scxmlraisetypes = scxml_scxmlraisetypes;
        this.scxml_scxmliftypes = scxml_scxmliftypes;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
        this.scxml_scxmlcanceltypes = scxml_scxmlcanceltypes;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
        this.scxml_scxmlcanceltypes = scxml_scxmlcanceltypes;
    }

    public String getAny1() {
        return any1;
    }

    public void setAny1(String any1) {
        this.any1 = any1;
    }
    public String getAny2() {
        return any2;
    }

    public void setAny2(String any2) {
        this.any2 = any2;
    }
    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getScxmlcoreexecutablecontent1() {
        return scxmlCoreExecutablecontent1;
    }

    public void setScxmlcoreexecutablecontent1(String scxmlCoreExecutablecontent1) {
        this.scxmlCoreExecutablecontent1 = scxmlCoreExecutablecontent1;
    }
    public String getScxmlcoreexecutablecontent() {
        return scxmlCoreExecutablecontent;
    }

    public void setScxmlcoreexecutablecontent(String scxmlCoreExecutablecontent) {
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
    }
    public String getScxmlcoreexecutablecontent2() {
        return scxmlCoreExecutablecontent2;
    }

    public void setScxmlcoreexecutablecontent2(String scxmlCoreExecutablecontent2) {
        this.scxmlCoreExecutablecontent2 = scxmlCoreExecutablecontent2;
    }

    public scxml_ScxmlFinalizeType getScxml_scxmlfinalizetype() {
        return scxml_scxmlfinalizetype;
    }

    public void setScxml_scxmlfinalizetype(scxml_ScxmlFinalizeType scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetype = scxml_scxmlfinalizetype;
    }
    public List<scxml_ScxmlRaiseType> getScxml_scxmlraisetypes() {
        return scxml_scxmlraisetypes;
    }

    public void addScxml_scxmlraisetype(Scxml_scxmlraisetype scxml_scxmlraisetype) {
        this.scxml_scxmlraisetypes.add(scxml_scxmlraisetype);
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }
    public List<scxml_ScxmlCancelType> getScxml_scxmlcanceltypes() {
        return scxml_scxmlcanceltypes;
    }

    public void addScxml_scxmlcanceltype(Scxml_scxmlcanceltype scxml_scxmlcanceltype) {
        this.scxml_scxmlcanceltypes.add(scxml_scxmlcanceltype);
    }
    public scxml_ScxmlElseType getScxml_scxmlelsetype() {
        return scxml_scxmlelsetype;
    }

    public void setScxml_scxmlelsetype(scxml_ScxmlElseType scxml_scxmlelsetype) {
        this.scxml_scxmlelsetype = scxml_scxmlelsetype;
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }
    public scxml_ScxmlIfType getScxml_scxmliftype() {
        return scxml_scxmliftype;
    }

    public void setScxml_scxmliftype(scxml_ScxmlIfType scxml_scxmliftype) {
        this.scxml_scxmliftype = scxml_scxmliftype;
    }
    public scxml_ScxmlIfType getScxml_scxmliftype() {
        return scxml_scxmliftype;
    }

    public void setScxml_scxmliftype(scxml_ScxmlIfType scxml_scxmliftype) {
        this.scxml_scxmliftype = scxml_scxmliftype;
    }
    public List<scxml_ScxmlRaiseType> getScxml_scxmlraisetypes() {
        return scxml_scxmlraisetypes;
    }

    public void addScxml_scxmlraisetype(Scxml_scxmlraisetype scxml_scxmlraisetype) {
        this.scxml_scxmlraisetypes.add(scxml_scxmlraisetype);
    }
    public scxml_ScxmlOnexitType getScxml_scxmlonexittype() {
        return scxml_scxmlonexittype;
    }

    public void setScxml_scxmlonexittype(scxml_ScxmlOnexitType scxml_scxmlonexittype) {
        this.scxml_scxmlonexittype = scxml_scxmlonexittype;
    }
    public List<scxml_ScxmlRaiseType> getScxml_scxmlraisetypes() {
        return scxml_scxmlraisetypes;
    }

    public void addScxml_scxmlraisetype(Scxml_scxmlraisetype scxml_scxmlraisetype) {
        this.scxml_scxmlraisetypes.add(scxml_scxmlraisetype);
    }
    public List<scxml_ScxmlIfType> getScxml_scxmliftypes() {
        return scxml_scxmliftypes;
    }

    public void addScxml_scxmliftype(Scxml_scxmliftype scxml_scxmliftype) {
        this.scxml_scxmliftypes.add(scxml_scxmliftype);
    }
    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }
    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }
    public List<scxml_ScxmlCancelType> getScxml_scxmlcanceltypes() {
        return scxml_scxmlcanceltypes;
    }

    public void addScxml_scxmlcanceltype(Scxml_scxmlcanceltype scxml_scxmlcanceltype) {
        this.scxml_scxmlcanceltypes.add(scxml_scxmlcanceltype);
    }
    public scxml_ScxmlElseifType getScxml_scxmlelseiftype() {
        return scxml_scxmlelseiftype;
    }

    public void setScxml_scxmlelseiftype(scxml_ScxmlElseifType scxml_scxmlelseiftype) {
        this.scxml_scxmlelseiftype = scxml_scxmlelseiftype;
    }
    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }
    public List<scxml_ScxmlCancelType> getScxml_scxmlcanceltypes() {
        return scxml_scxmlcanceltypes;
    }

    public void addScxml_scxmlcanceltype(Scxml_scxmlcanceltype scxml_scxmlcanceltype) {
        this.scxml_scxmlcanceltypes.add(scxml_scxmlcanceltype);
    }
    public scxml_ScxmlForeachType getScxml_scxmlforeachtype() {
        return scxml_scxmlforeachtype;
    }

    public void setScxml_scxmlforeachtype(scxml_ScxmlForeachType scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtype = scxml_scxmlforeachtype;
    }
    public scxml_ScxmlOnentryType getScxml_scxmlonentrytype() {
        return scxml_scxmlonentrytype;
    }

    public void setScxml_scxmlonentrytype(scxml_ScxmlOnentryType scxml_scxmlonentrytype) {
        this.scxml_scxmlonentrytype = scxml_scxmlonentrytype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}