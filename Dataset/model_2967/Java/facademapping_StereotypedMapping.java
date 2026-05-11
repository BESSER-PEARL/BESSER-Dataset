





import java.util.List;
import java.util.ArrayList;

public class facademapping_StereotypedMapping extends Mapping {

    private String kind;





    private List<facademapping_EObject> facademapping_eobjects;


    public facademapping_StereotypedMapping(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.facademapping_eobjects = new ArrayList<>();
    }

    public facademapping_StereotypedMapping(
        String kind        ArrayList<facademapping_EObject> facademapping_eobjects    ) {
        this.kind = kind;
        this.facademapping_eobjects = facademapping_eobjects;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<facademapping_EObject> getFacademapping_eobjects() {
        return facademapping_eobjects;
    }

    public void addFacademapping_eobject(Facademapping_eobject facademapping_eobject) {
        this.facademapping_eobjects.add(facademapping_eobject);
    }

}