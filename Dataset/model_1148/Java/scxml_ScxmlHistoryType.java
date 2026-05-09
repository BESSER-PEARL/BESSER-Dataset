





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlHistoryType  {

    private String anyAttribute;
    private String id;
    private String any1;
    private String scxmlExtraContent1;
    private String type;
    private String scxmlExtraContent;
    private String any;





    private scxml_ScxmlParallelType scxml_scxmlparalleltype;




    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlHistoryType(
        String anyAttribute,        String id,        String any1,        String scxmlExtraContent1,        String type,        String scxmlExtraContent,        String any    ) {
        this.anyAttribute = anyAttribute;
        this.id = id;
        this.any1 = any1;
        this.scxmlExtraContent1 = scxmlExtraContent1;
        this.type = type;
        this.scxmlExtraContent = scxmlExtraContent;
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
    public String getAny1() {
        return any1;
    }

    public void setAny1(String any1) {
        this.any1 = any1;
    }
    public String getScxmlextracontent1() {
        return scxmlExtraContent1;
    }

    public void setScxmlextracontent1(String scxmlExtraContent1) {
        this.scxmlExtraContent1 = scxmlExtraContent1;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public scxml_ScxmlParallelType getScxml_scxmlparalleltype() {
        return scxml_scxmlparalleltype;
    }

    public void setScxml_scxmlparalleltype(scxml_ScxmlParallelType scxml_scxmlparalleltype) {
        this.scxml_scxmlparalleltype = scxml_scxmlparalleltype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}