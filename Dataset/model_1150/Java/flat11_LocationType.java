





import java.util.List;
import java.util.ArrayList;

public class flat11_LocationType  {

    private String color;
    private String x;
    private String id;
    private String y;





    private flat11_NameType flat11_nametype;




    private flat11_CommittedType flat11_committedtype;




    private List<flat11_LabelType> flat11_labeltypes;




    private flat11_DocumentRoot flat11_documentroot;


    public flat11_LocationType(
        String color,        String x,        String id,        String y    ) {
        this.color = color;
        this.x = x;
        this.id = id;
        this.y = y;
        this.flat11_labeltypes = new ArrayList<>();
    }

    public flat11_LocationType(
        String color,        String x,        String id,        String y        ArrayList<flat11_LabelType> flat11_labeltypes    ) {
        this.color = color;
        this.x = x;
        this.id = id;
        this.y = y;
        this.flat11_labeltypes = flat11_labeltypes;
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
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public flat11_NameType getFlat11_nametype() {
        return flat11_nametype;
    }

    public void setFlat11_nametype(flat11_NameType flat11_nametype) {
        this.flat11_nametype = flat11_nametype;
    }
    public flat11_CommittedType getFlat11_committedtype() {
        return flat11_committedtype;
    }

    public void setFlat11_committedtype(flat11_CommittedType flat11_committedtype) {
        this.flat11_committedtype = flat11_committedtype;
    }
    public List<flat11_LabelType> getFlat11_labeltypes() {
        return flat11_labeltypes;
    }

    public void addFlat11_labeltype(Flat11_labeltype flat11_labeltype) {
        this.flat11_labeltypes.add(flat11_labeltype);
    }
    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}