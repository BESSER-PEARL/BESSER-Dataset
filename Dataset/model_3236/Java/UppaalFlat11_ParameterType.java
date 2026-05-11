





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_ParameterType  {

    private String y;
    private String x;
    private String mixed;





    private UppaalFlat11_TemplateType uppaalflat11_templatetype;




    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;


    public UppaalFlat11_ParameterType(
        String y,        String x,        String mixed    ) {
        this.y = y;
        this.x = x;
        this.mixed = mixed;
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
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public UppaalFlat11_TemplateType getUppaalflat11_templatetype() {
        return uppaalflat11_templatetype;
    }

    public void setUppaalflat11_templatetype(UppaalFlat11_TemplateType uppaalflat11_templatetype) {
        this.uppaalflat11_templatetype = uppaalflat11_templatetype;
    }
    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }

}