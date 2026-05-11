





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_LabelType  {

    private String kind;
    private String y;
    private String mixed;
    private String x;





    private UppaalFlat11_TransitionType uppaalflat11_transitiontype;




    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;


    public UppaalFlat11_LabelType(
        String kind,        String y,        String mixed,        String x    ) {
        this.kind = kind;
        this.y = y;
        this.mixed = mixed;
        this.x = x;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
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

    public UppaalFlat11_TransitionType getUppaalflat11_transitiontype() {
        return uppaalflat11_transitiontype;
    }

    public void setUppaalflat11_transitiontype(UppaalFlat11_TransitionType uppaalflat11_transitiontype) {
        this.uppaalflat11_transitiontype = uppaalflat11_transitiontype;
    }
    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }

}