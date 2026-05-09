





import java.util.List;
import java.util.ArrayList;

public class flat11_ParameterType  {

    private String value;
    private String y;
    private String x;





    private flat11_DocumentRoot flat11_documentroot;


    public flat11_ParameterType(
        String value,        String y,        String x    ) {
        this.value = value;
        this.y = y;
        this.x = x;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}