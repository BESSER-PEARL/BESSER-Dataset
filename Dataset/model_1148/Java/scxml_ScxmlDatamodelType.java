





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlDatamodelType  {

    private String any;
    private String anyAttribute;
    private String scxmlExtraContent;





    private List<scxml_ScxmlDataType> scxml_scxmldatatypes;




    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlDatamodelType(
        String any,        String anyAttribute,        String scxmlExtraContent    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlExtraContent = scxmlExtraContent;
        this.scxml_scxmldatatypes = new ArrayList<>();
    }

    public scxml_ScxmlDatamodelType(
        String any,        String anyAttribute,        String scxmlExtraContent        ArrayList<scxml_ScxmlDataType> scxml_scxmldatatypes    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlExtraContent = scxmlExtraContent;
        this.scxml_scxmldatatypes = scxml_scxmldatatypes;
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
    public String getScxmlextracontent() {
        return scxmlExtraContent;
    }

    public void setScxmlextracontent(String scxmlExtraContent) {
        this.scxmlExtraContent = scxmlExtraContent;
    }

    public List<scxml_ScxmlDataType> getScxml_scxmldatatypes() {
        return scxml_scxmldatatypes;
    }

    public void addScxml_scxmldatatype(Scxml_scxmldatatype scxml_scxmldatatype) {
        this.scxml_scxmldatatypes.add(scxml_scxmldatatype);
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}