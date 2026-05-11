





import java.util.List;
import java.util.ArrayList;

public class scxml_Assign  {

    private String expr;
    private String name;
    private String location;





    private scxml_ExecutableContent scxml_executablecontent;


    public scxml_Assign(
        String expr,        String name,        String location    ) {
        this.expr = expr;
        this.name = name;
        this.location = location;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public scxml_ExecutableContent getScxml_executablecontent() {
        return scxml_executablecontent;
    }

    public void setScxml_executablecontent(scxml_ExecutableContent scxml_executablecontent) {
        this.scxml_executablecontent = scxml_executablecontent;
    }

}