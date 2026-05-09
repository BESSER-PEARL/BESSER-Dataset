





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlParamType  {

    private String expr;
    private String anyAttribute;
    private String scxmlExtraContent;
    private String any;
    private String name;





    private scxml_ScxmlSendType scxml_scxmlsendtype;


    public scxml_ScxmlParamType(
        String expr,        String anyAttribute,        String scxmlExtraContent,        String any,        String name    ) {
        this.expr = expr;
        this.anyAttribute = anyAttribute;
        this.scxmlExtraContent = scxmlExtraContent;
        this.any = any;
        this.name = name;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
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
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public scxml_ScxmlSendType getScxml_scxmlsendtype() {
        return scxml_scxmlsendtype;
    }

    public void setScxml_scxmlsendtype(scxml_ScxmlSendType scxml_scxmlsendtype) {
        this.scxml_scxmlsendtype = scxml_scxmlsendtype;
    }

}