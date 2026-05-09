





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlFinalType  {

    private String any;
    private String scxmlFinalMix;
    private String id;
    private String anyAttribute;





    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlFinalType(
        String any,        String scxmlFinalMix,        String id,        String anyAttribute    ) {
        this.any = any;
        this.scxmlFinalMix = scxmlFinalMix;
        this.id = id;
        this.anyAttribute = anyAttribute;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getScxmlfinalmix() {
        return scxmlFinalMix;
    }

    public void setScxmlfinalmix(String scxmlFinalMix) {
        this.scxmlFinalMix = scxmlFinalMix;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}