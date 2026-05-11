





import java.util.List;
import java.util.ArrayList;

public class Uppaal_TransitionType  {

    private String y;
    private String x;
    private String id;
    private String color;





    private Uppaal_TargetType uppaal_targettype;




    private Uppaal_SourceType uppaal_sourcetype;




    private List<Uppaal_LabelType> uppaal_labeltypes;




    private List<Uppaal_NailType> uppaal_nailtypes;




    private Uppaal_DocumentRoot uppaal_documentroot;


    public Uppaal_TransitionType(
        String y,        String x,        String id,        String color    ) {
        this.y = y;
        this.x = x;
        this.id = id;
        this.color = color;
        this.uppaal_labeltypes = new ArrayList<>();
        this.uppaal_nailtypes = new ArrayList<>();
    }

    public Uppaal_TransitionType(
        String y,        String x,        String id,        String color        ArrayList<Uppaal_LabelType> uppaal_labeltypes,        ArrayList<Uppaal_NailType> uppaal_nailtypes    ) {
        this.y = y;
        this.x = x;
        this.id = id;
        this.color = color;
        this.uppaal_labeltypes = uppaal_labeltypes;
        this.uppaal_nailtypes = uppaal_nailtypes;
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

    public Uppaal_TargetType getUppaal_targettype() {
        return uppaal_targettype;
    }

    public void setUppaal_targettype(Uppaal_TargetType uppaal_targettype) {
        this.uppaal_targettype = uppaal_targettype;
    }
    public Uppaal_SourceType getUppaal_sourcetype() {
        return uppaal_sourcetype;
    }

    public void setUppaal_sourcetype(Uppaal_SourceType uppaal_sourcetype) {
        this.uppaal_sourcetype = uppaal_sourcetype;
    }
    public List<Uppaal_LabelType> getUppaal_labeltypes() {
        return uppaal_labeltypes;
    }

    public void addUppaal_labeltype(Uppaal_labeltype uppaal_labeltype) {
        this.uppaal_labeltypes.add(uppaal_labeltype);
    }
    public List<Uppaal_NailType> getUppaal_nailtypes() {
        return uppaal_nailtypes;
    }

    public void addUppaal_nailtype(Uppaal_nailtype uppaal_nailtype) {
        this.uppaal_nailtypes.add(uppaal_nailtype);
    }
    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}