





import java.util.List;
import java.util.ArrayList;

public class Uppaal_DocumentRoot  {

    private String urgent;
    private String committed;
    private String mixed;





    private List<Uppaal_DeclarationType> uppaal_declarationtypes;


    public Uppaal_DocumentRoot(
        String urgent,        String committed,        String mixed    ) {
        this.urgent = urgent;
        this.committed = committed;
        this.mixed = mixed;
        this.uppaal_declarationtypes = new ArrayList<>();
    }

    public Uppaal_DocumentRoot(
        String urgent,        String committed,        String mixed        ArrayList<Uppaal_DeclarationType> uppaal_declarationtypes    ) {
        this.urgent = urgent;
        this.committed = committed;
        this.mixed = mixed;
        this.uppaal_declarationtypes = uppaal_declarationtypes;
    }

    public String getUrgent() {
        return urgent;
    }

    public void setUrgent(String urgent) {
        this.urgent = urgent;
    }
    public String getCommitted() {
        return committed;
    }

    public void setCommitted(String committed) {
        this.committed = committed;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<Uppaal_DeclarationType> getUppaal_declarationtypes() {
        return uppaal_declarationtypes;
    }

    public void addUppaal_declarationtype(Uppaal_declarationtype uppaal_declarationtype) {
        this.uppaal_declarationtypes.add(uppaal_declarationtype);
    }

}