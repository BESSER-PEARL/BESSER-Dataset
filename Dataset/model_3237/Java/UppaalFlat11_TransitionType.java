





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_TransitionType  {

    private String id;
    private String color;
    private String y;
    private String x;





    private UppaalFlat11_TemplateType uppaalflat11_templatetype;




    private UppaalFlat11_TargetType uppaalflat11_targettype;




    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;




    private List<UppaalFlat11_LabelType> uppaalflat11_labeltypes;


    public UppaalFlat11_TransitionType(
        String id,        String color,        String y,        String x    ) {
        this.id = id;
        this.color = color;
        this.y = y;
        this.x = x;
        this.uppaalflat11_labeltypes = new ArrayList<>();
    }

    public UppaalFlat11_TransitionType(
        String id,        String color,        String y,        String x        ArrayList<UppaalFlat11_LabelType> uppaalflat11_labeltypes    ) {
        this.id = id;
        this.color = color;
        this.y = y;
        this.x = x;
        this.uppaalflat11_labeltypes = uppaalflat11_labeltypes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
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

    public UppaalFlat11_TemplateType getUppaalflat11_templatetype() {
        return uppaalflat11_templatetype;
    }

    public void setUppaalflat11_templatetype(UppaalFlat11_TemplateType uppaalflat11_templatetype) {
        this.uppaalflat11_templatetype = uppaalflat11_templatetype;
    }
    public UppaalFlat11_TargetType getUppaalflat11_targettype() {
        return uppaalflat11_targettype;
    }

    public void setUppaalflat11_targettype(UppaalFlat11_TargetType uppaalflat11_targettype) {
        this.uppaalflat11_targettype = uppaalflat11_targettype;
    }
    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }
    public List<UppaalFlat11_LabelType> getUppaalflat11_labeltypes() {
        return uppaalflat11_labeltypes;
    }

    public void addUppaalflat11_labeltype(Uppaalflat11_labeltype uppaalflat11_labeltype) {
        this.uppaalflat11_labeltypes.add(uppaalflat11_labeltype);
    }

}