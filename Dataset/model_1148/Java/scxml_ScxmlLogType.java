





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlLogType  {

    private String any;
    private String anyAttribute;
    private String expr;
    private String scxmlExtraContent;
    private String label;





    private scxml_DocumentRoot scxml_documentroot;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private scxml_ScxmlOnentryType scxml_scxmlonentrytype;




    private scxml_ScxmlForeachType scxml_scxmlforeachtype;




    private scxml_ScxmlIfType scxml_scxmliftype;




    private scxml_ScxmlFinalizeType scxml_scxmlfinalizetype;




    private scxml_ScxmlOnexitType scxml_scxmlonexittype;


    public scxml_ScxmlLogType(
        String any,        String anyAttribute,        String expr,        String scxmlExtraContent,        String label    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.expr = expr;
        this.scxmlExtraContent = scxmlExtraContent;
        this.label = label;
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
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getScxmlextracontent() {
        return scxmlExtraContent;
    }

    public void setScxmlextracontent(String scxmlExtraContent) {
        this.scxmlExtraContent = scxmlExtraContent;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
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
    public scxml_ScxmlOnentryType getScxml_scxmlonentrytype() {
        return scxml_scxmlonentrytype;
    }

    public void setScxml_scxmlonentrytype(scxml_ScxmlOnentryType scxml_scxmlonentrytype) {
        this.scxml_scxmlonentrytype = scxml_scxmlonentrytype;
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
    public scxml_ScxmlFinalizeType getScxml_scxmlfinalizetype() {
        return scxml_scxmlfinalizetype;
    }

    public void setScxml_scxmlfinalizetype(scxml_ScxmlFinalizeType scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetype = scxml_scxmlfinalizetype;
    }
    public scxml_ScxmlOnexitType getScxml_scxmlonexittype() {
        return scxml_scxmlonexittype;
    }

    public void setScxml_scxmlonexittype(scxml_ScxmlOnexitType scxml_scxmlonexittype) {
        this.scxml_scxmlonexittype = scxml_scxmlonexittype;
    }

}