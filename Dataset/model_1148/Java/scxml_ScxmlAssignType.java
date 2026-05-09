





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlAssignType  {

    private String location;
    private String mixed;
    private String attr;
    private String anyAttribute;
    private String type;
    private String expr;
    private String any;





    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlAssignType(
        String location,        String mixed,        String attr,        String anyAttribute,        String type,        String expr,        String any    ) {
        this.location = location;
        this.mixed = mixed;
        this.attr = attr;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.expr = expr;
        this.any = any;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getAttr() {
        return attr;
    }

    public void setAttr(String attr) {
        this.attr = attr;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}