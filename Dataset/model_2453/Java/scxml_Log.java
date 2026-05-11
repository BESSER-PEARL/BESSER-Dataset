





import java.util.List;
import java.util.ArrayList;

public class scxml_Log  {

    private String label;
    private String level;
    private String expr;





    private scxml_If scxml_if;


    public scxml_Log(
        String label,        String level,        String expr    ) {
        this.label = label;
        this.level = level;
        this.expr = expr;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }

    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }

}