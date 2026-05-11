





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_LocationType  {

    private String color;
    private String x;
    private String y;
    private String id;





    private List<UppaalFlat11_LabelType> uppaalflat11_labeltypes;




    private UppaalFlat11_TemplateType uppaalflat11_templatetype;




    private UppaalFlat11_CommittedType uppaalflat11_committedtype;




    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;


    public UppaalFlat11_LocationType(
        String color,        String x,        String y,        String id    ) {
        this.color = color;
        this.x = x;
        this.y = y;
        this.id = id;
        this.uppaalflat11_labeltypes = new ArrayList<>();
    }

    public UppaalFlat11_LocationType(
        String color,        String x,        String y,        String id        ArrayList<UppaalFlat11_LabelType> uppaalflat11_labeltypes    ) {
        this.color = color;
        this.x = x;
        this.y = y;
        this.id = id;
        this.uppaalflat11_labeltypes = uppaalflat11_labeltypes;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<UppaalFlat11_LabelType> getUppaalflat11_labeltypes() {
        return uppaalflat11_labeltypes;
    }

    public void addUppaalflat11_labeltype(Uppaalflat11_labeltype uppaalflat11_labeltype) {
        this.uppaalflat11_labeltypes.add(uppaalflat11_labeltype);
    }
    public UppaalFlat11_TemplateType getUppaalflat11_templatetype() {
        return uppaalflat11_templatetype;
    }

    public void setUppaalflat11_templatetype(UppaalFlat11_TemplateType uppaalflat11_templatetype) {
        this.uppaalflat11_templatetype = uppaalflat11_templatetype;
    }
    public UppaalFlat11_CommittedType getUppaalflat11_committedtype() {
        return uppaalflat11_committedtype;
    }

    public void setUppaalflat11_committedtype(UppaalFlat11_CommittedType uppaalflat11_committedtype) {
        this.uppaalflat11_committedtype = uppaalflat11_committedtype;
    }
    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }

}