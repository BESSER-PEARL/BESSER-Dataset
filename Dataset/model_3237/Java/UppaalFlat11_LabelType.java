





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_LabelType  {

    private String mixed;
    private String y;
    private String kind;
    private String x;





    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;


    public UppaalFlat11_LabelType(
        String mixed,        String y,        String kind,        String x    ) {
        this.mixed = mixed;
        this.y = y;
        this.kind = kind;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }

}