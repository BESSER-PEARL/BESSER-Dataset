





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlContentType  {

    private String anyAttribute;
    private String mixed;
    private String any;
    private String expr;





    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlContentType(
        String anyAttribute,        String mixed,        String any,        String expr    ) {
        this.anyAttribute = anyAttribute;
        this.mixed = mixed;
        this.any = any;
        this.expr = expr;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}