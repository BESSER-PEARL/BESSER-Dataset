





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlParamType  {

    private String scxmlExtraContent;
    private String any;
    private String expr;
    private String name;
    private String anyAttribute;
    private String location;





    private scxml_ScxmlDonedataType scxml_scxmldonedatatype;




    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlParamType(
        String scxmlExtraContent,        String any,        String expr,        String name,        String anyAttribute,        String location    ) {
        this.scxmlExtraContent = scxmlExtraContent;
        this.any = any;
        this.expr = expr;
        this.name = name;
        this.anyAttribute = anyAttribute;
        this.location = location;
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
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public scxml_ScxmlDonedataType getScxml_scxmldonedatatype() {
        return scxml_scxmldonedatatype;
    }

    public void setScxml_scxmldonedatatype(scxml_ScxmlDonedataType scxml_scxmldonedatatype) {
        this.scxml_scxmldonedatatype = scxml_scxmldonedatatype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}