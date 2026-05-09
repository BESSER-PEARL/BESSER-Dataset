





import java.util.List;
import java.util.ArrayList;

public class flat11_LabelType  {

    private String x;
    private String y;
    private String value;
    private String kind;





    private flat11_DocumentRoot flat11_documentroot;




    private flat11_LocationType flat11_locationtype;


    public flat11_LabelType(
        String x,        String y,        String value,        String kind    ) {
        this.x = x;
        this.y = y;
        this.value = value;
        this.kind = kind;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }
    public flat11_LocationType getFlat11_locationtype() {
        return flat11_locationtype;
    }

    public void setFlat11_locationtype(flat11_LocationType flat11_locationtype) {
        this.flat11_locationtype = flat11_locationtype;
    }

}