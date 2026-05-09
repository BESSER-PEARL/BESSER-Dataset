





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlRaiseType  {

    private String event;
    private String anyAttribute;





    private scxml_ScxmlFinalizeType scxml_scxmlfinalizetype;




    private scxml_ScxmlOnentryType scxml_scxmlonentrytype;




    private scxml_ScxmlOnexitType scxml_scxmlonexittype;




    private scxml_DocumentRoot scxml_documentroot;




    private scxml_ScxmlForeachType scxml_scxmlforeachtype;


    public scxml_ScxmlRaiseType(
        String event,        String anyAttribute    ) {
        this.event = event;
        this.anyAttribute = anyAttribute;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public scxml_ScxmlFinalizeType getScxml_scxmlfinalizetype() {
        return scxml_scxmlfinalizetype;
    }

    public void setScxml_scxmlfinalizetype(scxml_ScxmlFinalizeType scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetype = scxml_scxmlfinalizetype;
    }
    public scxml_ScxmlOnentryType getScxml_scxmlonentrytype() {
        return scxml_scxmlonentrytype;
    }

    public void setScxml_scxmlonentrytype(scxml_ScxmlOnentryType scxml_scxmlonentrytype) {
        this.scxml_scxmlonentrytype = scxml_scxmlonentrytype;
    }
    public scxml_ScxmlOnexitType getScxml_scxmlonexittype() {
        return scxml_scxmlonexittype;
    }

    public void setScxml_scxmlonexittype(scxml_ScxmlOnexitType scxml_scxmlonexittype) {
        this.scxml_scxmlonexittype = scxml_scxmlonexittype;
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

}