





import java.util.List;
import java.util.ArrayList;

public class scxml_Data extends DescriptionContainer {

    private String src;
    private String id;
    private String expr;





    private scxml_Datamodel scxml_datamodel;


    public scxml_Data(
        String src,        String id,        String expr    ) {
        super(
        );
        this.src = src;
        this.id = id;
        this.expr = expr;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }

    public scxml_Datamodel getScxml_datamodel() {
        return scxml_datamodel;
    }

    public void setScxml_datamodel(scxml_Datamodel scxml_datamodel) {
        this.scxml_datamodel = scxml_datamodel;
    }

}