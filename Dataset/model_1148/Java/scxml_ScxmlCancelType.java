





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlCancelType  {

    private String sendid;
    private String anyAttribute;
    private String scxmlExtraContent;
    private String sendidexpr;
    private String any;





    private scxml_ScxmlFinalizeType scxml_scxmlfinalizetype;




    private scxml_ScxmlForeachType scxml_scxmlforeachtype;




    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlCancelType(
        String sendid,        String anyAttribute,        String scxmlExtraContent,        String sendidexpr,        String any    ) {
        this.sendid = sendid;
        this.anyAttribute = anyAttribute;
        this.scxmlExtraContent = scxmlExtraContent;
        this.sendidexpr = sendidexpr;
        this.any = any;
    }


    public String getSendid() {
        return sendid;
    }

    public void setSendid(String sendid) {
        this.sendid = sendid;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getScxmlextracontent() {
        return scxmlExtraContent;
    }

    public void setScxmlextracontent(String scxmlExtraContent) {
        this.scxmlExtraContent = scxmlExtraContent;
    }
    public String getSendidexpr() {
        return sendidexpr;
    }

    public void setSendidexpr(String sendidexpr) {
        this.sendidexpr = sendidexpr;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public scxml_ScxmlFinalizeType getScxml_scxmlfinalizetype() {
        return scxml_scxmlfinalizetype;
    }

    public void setScxml_scxmlfinalizetype(scxml_ScxmlFinalizeType scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetype = scxml_scxmlfinalizetype;
    }
    public scxml_ScxmlForeachType getScxml_scxmlforeachtype() {
        return scxml_scxmlforeachtype;
    }

    public void setScxml_scxmlforeachtype(scxml_ScxmlForeachType scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtype = scxml_scxmlforeachtype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}