





import java.util.List;
import java.util.ArrayList;

public class uppaal_TransitionType  {

    private String y;
    private String color;
    private String x;
    private String id;





    private uppaal_SourceType uppaal_sourcetype;




    private uppaal_DocumentRoot uppaal_documentroot;




    private List<uppaal_LabelType> uppaal_labeltypes;




    private List<uppaal_NailType> uppaal_nailtypes;




    private uppaal_TemplateType uppaal_templatetype;




    private uppaal_TargetType uppaal_targettype;


    public uppaal_TransitionType(
        String y,        String color,        String x,        String id    ) {
        this.y = y;
        this.color = color;
        this.x = x;
        this.id = id;
        this.uppaal_labeltypes = new ArrayList<>();
        this.uppaal_nailtypes = new ArrayList<>();
    }

    public uppaal_TransitionType(
        String y,        String color,        String x,        String id        ArrayList<uppaal_LabelType> uppaal_labeltypes,        ArrayList<uppaal_NailType> uppaal_nailtypes    ) {
        this.y = y;
        this.color = color;
        this.x = x;
        this.id = id;
        this.uppaal_labeltypes = uppaal_labeltypes;
        this.uppaal_nailtypes = uppaal_nailtypes;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public uppaal_SourceType getUppaal_sourcetype() {
        return uppaal_sourcetype;
    }

    public void setUppaal_sourcetype(uppaal_SourceType uppaal_sourcetype) {
        this.uppaal_sourcetype = uppaal_sourcetype;
    }
    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }
    public List<uppaal_LabelType> getUppaal_labeltypes() {
        return uppaal_labeltypes;
    }

    public void addUppaal_labeltype(Uppaal_labeltype uppaal_labeltype) {
        this.uppaal_labeltypes.add(uppaal_labeltype);
    }
    public List<uppaal_NailType> getUppaal_nailtypes() {
        return uppaal_nailtypes;
    }

    public void addUppaal_nailtype(Uppaal_nailtype uppaal_nailtype) {
        this.uppaal_nailtypes.add(uppaal_nailtype);
    }
    public uppaal_TemplateType getUppaal_templatetype() {
        return uppaal_templatetype;
    }

    public void setUppaal_templatetype(uppaal_TemplateType uppaal_templatetype) {
        this.uppaal_templatetype = uppaal_templatetype;
    }
    public uppaal_TargetType getUppaal_targettype() {
        return uppaal_targettype;
    }

    public void setUppaal_targettype(uppaal_TargetType uppaal_targettype) {
        this.uppaal_targettype = uppaal_targettype;
    }

}