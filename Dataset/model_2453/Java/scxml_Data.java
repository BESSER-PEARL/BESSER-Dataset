





import java.util.List;
import java.util.ArrayList;

public class scxml_Data  {

    private String expr;
    private String id;
    private String src;





    private scxml_Content scxml_content;




    private scxml_DataModel scxml_datamodel;


    public scxml_Data(
        String expr,        String id,        String src    ) {
        this.expr = expr;
        this.id = id;
        this.src = src;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }

    public scxml_Content getScxml_content() {
        return scxml_content;
    }

    public void setScxml_content(scxml_Content scxml_content) {
        this.scxml_content = scxml_content;
    }
    public scxml_DataModel getScxml_datamodel() {
        return scxml_datamodel;
    }

    public void setScxml_datamodel(scxml_DataModel scxml_datamodel) {
        this.scxml_datamodel = scxml_datamodel;
    }

}