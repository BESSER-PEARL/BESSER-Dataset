





import java.util.List;
import java.util.ArrayList;

public class flat11_LabelType  {

    private String x;
    private String kind;
    private String value;
    private String y;





    private flat11_DocumentRoot flat11_documentroot;


    public flat11_LabelType(
        String x,        String kind,        String value,        String y    ) {
        this.x = x;
        this.kind = kind;
        this.value = value;
        this.y = y;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}