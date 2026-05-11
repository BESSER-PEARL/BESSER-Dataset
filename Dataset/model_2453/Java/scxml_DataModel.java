





import java.util.List;
import java.util.ArrayList;

public class scxml_DataModel  {

    private String schema;





    private scxml_NamedElement scxml_namedelement;


    public scxml_DataModel(
        String schema    ) {
        this.schema = schema;
    }


    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }

    public scxml_NamedElement getScxml_namedelement() {
        return scxml_namedelement;
    }

    public void setScxml_namedelement(scxml_NamedElement scxml_namedelement) {
        this.scxml_namedelement = scxml_namedelement;
    }

}