





import java.util.List;
import java.util.ArrayList;

public class scxml_Param  {

    private String expr;
    private String name;





    private scxml_If scxml_if;




    private scxml_Invoke scxml_invoke;




    private scxml_Donedata scxml_donedata;


    public scxml_Param(
        String expr,        String name    ) {
        this.expr = expr;
        this.name = name;
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

    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }
    public scxml_Invoke getScxml_invoke() {
        return scxml_invoke;
    }

    public void setScxml_invoke(scxml_Invoke scxml_invoke) {
        this.scxml_invoke = scxml_invoke;
    }
    public scxml_Donedata getScxml_donedata() {
        return scxml_donedata;
    }

    public void setScxml_donedata(scxml_Donedata scxml_donedata) {
        this.scxml_donedata = scxml_donedata;
    }

}