





import java.util.List;
import java.util.ArrayList;

public class scxml_Param  {

    private String name;
    private String expr;



    public scxml_Param(
        String name,        String expr    ) {
        this.name = name;
        this.expr = expr;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }


}