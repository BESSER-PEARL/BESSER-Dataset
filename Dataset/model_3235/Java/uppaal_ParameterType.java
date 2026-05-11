





import java.util.List;
import java.util.ArrayList;

public class uppaal_ParameterType  {

    private String y;
    private String mixed;
    private String x;





    private uppaal_DocumentRoot uppaal_documentroot;


    public uppaal_ParameterType(
        String y,        String mixed,        String x    ) {
        this.y = y;
        this.mixed = mixed;
        this.x = x;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}