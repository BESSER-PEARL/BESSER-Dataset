





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlDataType  {

    private String expr;
    private String src;
    private String any;
    private String anyAttribute;
    private String id;
    private String mixed;





    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlDataType(
        String expr,        String src,        String any,        String anyAttribute,        String id,        String mixed    ) {
        this.expr = expr;
        this.src = src;
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.id = id;
        this.mixed = mixed;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}