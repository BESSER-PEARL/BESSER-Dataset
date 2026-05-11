





import java.util.List;
import java.util.ArrayList;

public class scxml_Assign  {

    private String dataid;
    private String location;
    private String expr;



    public scxml_Assign(
        String dataid,        String location,        String expr    ) {
        this.dataid = dataid;
        this.location = location;
        this.expr = expr;
    }


    public String getDataid() {
        return dataid;
    }

    public void setDataid(String dataid) {
        this.dataid = dataid;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }


}