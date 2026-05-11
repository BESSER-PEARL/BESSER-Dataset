





import java.util.List;
import java.util.ArrayList;

public class Uppaal_LocationType  {

    private String committed;
    private String id;
    private String y;
    private String x;
    private String urgent;
    private String color;





    private Uppaal_DocumentRoot uppaal_documentroot;




    private List<Uppaal_LabelType> uppaal_labeltypes;


    public Uppaal_LocationType(
        String committed,        String id,        String y,        String x,        String urgent,        String color    ) {
        this.committed = committed;
        this.id = id;
        this.y = y;
        this.x = x;
        this.urgent = urgent;
        this.color = color;
        this.uppaal_labeltypes = new ArrayList<>();
    }

    public Uppaal_LocationType(
        String committed,        String id,        String y,        String x,        String urgent,        String color        ArrayList<Uppaal_LabelType> uppaal_labeltypes    ) {
        this.committed = committed;
        this.id = id;
        this.y = y;
        this.x = x;
        this.urgent = urgent;
        this.color = color;
        this.uppaal_labeltypes = uppaal_labeltypes;
    }

    public String getCommitted() {
        return committed;
    }

    public void setCommitted(String committed) {
        this.committed = committed;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getUrgent() {
        return urgent;
    }

    public void setUrgent(String urgent) {
        this.urgent = urgent;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }
    public List<Uppaal_LabelType> getUppaal_labeltypes() {
        return uppaal_labeltypes;
    }

    public void addUppaal_labeltype(Uppaal_labeltype uppaal_labeltype) {
        this.uppaal_labeltypes.add(uppaal_labeltype);
    }

}