





import java.util.List;
import java.util.ArrayList;

public class Uppaal_LabelType  {

    private String x;
    private String mixed;
    private String y;
    private String kind;





    private Uppaal_DocumentRoot uppaal_documentroot;


    public Uppaal_LabelType(
        String x,        String mixed,        String y,        String kind    ) {
        this.x = x;
        this.mixed = mixed;
        this.y = y;
        this.kind = kind;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}