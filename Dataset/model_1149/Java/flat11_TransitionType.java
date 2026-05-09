





import java.util.List;
import java.util.ArrayList;

public class flat11_TransitionType  {

    private String controllable;
    private String color;
    private String action;
    private String y;
    private String id;
    private String x;





    private List<flat11_NailType> flat11_nailtypes;




    private flat11_TargetType flat11_targettype;




    private flat11_TemplateType flat11_templatetype;




    private flat11_DocumentRoot flat11_documentroot;




    private flat11_SourceType flat11_sourcetype;




    private List<flat11_LabelType> flat11_labeltypes;


    public flat11_TransitionType(
        String controllable,        String color,        String action,        String y,        String id,        String x    ) {
        this.controllable = controllable;
        this.color = color;
        this.action = action;
        this.y = y;
        this.id = id;
        this.x = x;
        this.flat11_nailtypes = new ArrayList<>();
        this.flat11_labeltypes = new ArrayList<>();
    }

    public flat11_TransitionType(
        String controllable,        String color,        String action,        String y,        String id,        String x        ArrayList<flat11_NailType> flat11_nailtypes,        ArrayList<flat11_LabelType> flat11_labeltypes    ) {
        this.controllable = controllable;
        this.color = color;
        this.action = action;
        this.y = y;
        this.id = id;
        this.x = x;
        this.flat11_nailtypes = flat11_nailtypes;
        this.flat11_labeltypes = flat11_labeltypes;
    }

    public String getControllable() {
        return controllable;
    }

    public void setControllable(String controllable) {
        this.controllable = controllable;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public List<flat11_NailType> getFlat11_nailtypes() {
        return flat11_nailtypes;
    }

    public void addFlat11_nailtype(Flat11_nailtype flat11_nailtype) {
        this.flat11_nailtypes.add(flat11_nailtype);
    }
    public flat11_TargetType getFlat11_targettype() {
        return flat11_targettype;
    }

    public void setFlat11_targettype(flat11_TargetType flat11_targettype) {
        this.flat11_targettype = flat11_targettype;
    }
    public flat11_TemplateType getFlat11_templatetype() {
        return flat11_templatetype;
    }

    public void setFlat11_templatetype(flat11_TemplateType flat11_templatetype) {
        this.flat11_templatetype = flat11_templatetype;
    }
    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }
    public flat11_SourceType getFlat11_sourcetype() {
        return flat11_sourcetype;
    }

    public void setFlat11_sourcetype(flat11_SourceType flat11_sourcetype) {
        this.flat11_sourcetype = flat11_sourcetype;
    }
    public List<flat11_LabelType> getFlat11_labeltypes() {
        return flat11_labeltypes;
    }

    public void addFlat11_labeltype(Flat11_labeltype flat11_labeltype) {
        this.flat11_labeltypes.add(flat11_labeltype);
    }

}