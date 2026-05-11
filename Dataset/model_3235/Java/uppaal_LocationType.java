





import java.util.List;
import java.util.ArrayList;

public class uppaal_LocationType  {

    private String id;
    private String y;
    private String color;
    private String x;





    private uppaal_NameType uppaal_nametype;




    private List<uppaal_LabelType> uppaal_labeltypes;




    private uppaal_DocumentRoot uppaal_documentroot;




    private uppaal_CommittedType uppaal_committedtype;


    public uppaal_LocationType(
        String id,        String y,        String color,        String x    ) {
        this.id = id;
        this.y = y;
        this.color = color;
        this.x = x;
        this.uppaal_labeltypes = new ArrayList<>();
    }

    public uppaal_LocationType(
        String id,        String y,        String color,        String x        ArrayList<uppaal_LabelType> uppaal_labeltypes    ) {
        this.id = id;
        this.y = y;
        this.color = color;
        this.x = x;
        this.uppaal_labeltypes = uppaal_labeltypes;
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

    public uppaal_NameType getUppaal_nametype() {
        return uppaal_nametype;
    }

    public void setUppaal_nametype(uppaal_NameType uppaal_nametype) {
        this.uppaal_nametype = uppaal_nametype;
    }
    public List<uppaal_LabelType> getUppaal_labeltypes() {
        return uppaal_labeltypes;
    }

    public void addUppaal_labeltype(Uppaal_labeltype uppaal_labeltype) {
        this.uppaal_labeltypes.add(uppaal_labeltype);
    }
    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }
    public uppaal_CommittedType getUppaal_committedtype() {
        return uppaal_committedtype;
    }

    public void setUppaal_committedtype(uppaal_CommittedType uppaal_committedtype) {
        this.uppaal_committedtype = uppaal_committedtype;
    }

}