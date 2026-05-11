





import java.util.List;
import java.util.ArrayList;

public class scxml_Log  {

    private String expr;
    private String level;
    private String label;



    public scxml_Log(
        String expr,        String level,        String label    ) {
        this.expr = expr;
        this.level = level;
        this.label = label;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}