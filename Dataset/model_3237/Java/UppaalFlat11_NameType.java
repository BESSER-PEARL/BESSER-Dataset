





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_NameType  {

    private String mixed;
    private String x;
    private String y;





    private UppaalFlat11_TemplateType uppaalflat11_templatetype;




    private UppaalFlat11_LocationType uppaalflat11_locationtype;




    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;


    public UppaalFlat11_NameType(
        String mixed,        String x,        String y    ) {
        this.mixed = mixed;
        this.x = x;
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
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public UppaalFlat11_TemplateType getUppaalflat11_templatetype() {
        return uppaalflat11_templatetype;
    }

    public void setUppaalflat11_templatetype(UppaalFlat11_TemplateType uppaalflat11_templatetype) {
        this.uppaalflat11_templatetype = uppaalflat11_templatetype;
    }
    public UppaalFlat11_LocationType getUppaalflat11_locationtype() {
        return uppaalflat11_locationtype;
    }

    public void setUppaalflat11_locationtype(UppaalFlat11_LocationType uppaalflat11_locationtype) {
        this.uppaalflat11_locationtype = uppaalflat11_locationtype;
    }
    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }

}