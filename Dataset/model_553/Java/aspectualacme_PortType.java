





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_PortType extends TypeDefinition {






    private List<aspectualacme_PortType> aspectualacme_porttypes;




    private aspectualacme_Family aspectualacme_family;




    private aspectualacme_Family aspectualacme_family;


    public aspectualacme_PortType(
    ) {
        super(
        );
        this.aspectualacme_porttypes = new ArrayList<>();
    }

    public aspectualacme_PortType(
        ArrayList<aspectualacme_PortType> aspectualacme_porttypes    ) {
        this.aspectualacme_porttypes = aspectualacme_porttypes;
    }


    public List<aspectualacme_PortType> getAspectualacme_porttypes() {
        return aspectualacme_porttypes;
    }

    public void addAspectualacme_porttype(Aspectualacme_porttype aspectualacme_porttype) {
        this.aspectualacme_porttypes.add(aspectualacme_porttype);
    }
    public aspectualacme_Family getAspectualacme_family() {
        return aspectualacme_family;
    }

    public void setAspectualacme_family(aspectualacme_Family aspectualacme_family) {
        this.aspectualacme_family = aspectualacme_family;
    }
    public aspectualacme_Family getAspectualacme_family() {
        return aspectualacme_family;
    }

    public void setAspectualacme_family(aspectualacme_Family aspectualacme_family) {
        this.aspectualacme_family = aspectualacme_family;
    }

}