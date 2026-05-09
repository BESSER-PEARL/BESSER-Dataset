





import java.util.List;
import java.util.ArrayList;

public class flat11_ParameterType  {

    private String x;
    private String y;
    private String value;





    private flat11_DocumentRoot flat11_documentroot;


    public flat11_ParameterType(
        String x,        String y,        String value    ) {
        this.x = x;
        this.y = y;
        this.value = value;
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

    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}