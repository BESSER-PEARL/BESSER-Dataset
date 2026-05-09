





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlElseifType  {

    private String anyAttribute;
    private String cond;





    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlElseifType(
        String anyAttribute,        String cond    ) {
        this.anyAttribute = anyAttribute;
        this.cond = cond;
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

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}