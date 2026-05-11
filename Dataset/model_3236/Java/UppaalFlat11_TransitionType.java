





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_TransitionType  {

    private String id;
    private String x;
    private String y;
    private String color;





    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;




    private UppaalFlat11_TemplateType uppaalflat11_templatetype;


    public UppaalFlat11_TransitionType(
        String id,        String x,        String y,        String color    ) {
        this.id = id;
        this.x = x;
        this.y = y;
        this.color = color;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }
    public UppaalFlat11_TemplateType getUppaalflat11_templatetype() {
        return uppaalflat11_templatetype;
    }

    public void setUppaalflat11_templatetype(UppaalFlat11_TemplateType uppaalflat11_templatetype) {
        this.uppaalflat11_templatetype = uppaalflat11_templatetype;
    }

}