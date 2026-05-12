





import java.util.List;
import java.util.ArrayList;

public class Ant_ClassPath extends Set {

    private String refid;





    private List<Ant_PathElement> ant_pathelements;


    public Ant_ClassPath(
        String refid    ) {
        super(
        );
        this.refid = refid;
        this.ant_pathelements = new ArrayList<>();
    }

    public Ant_ClassPath(
        String refid        ArrayList<Ant_PathElement> ant_pathelements    ) {
        this.refid = refid;
        this.ant_pathelements = ant_pathelements;
    }

    public String getRefid() {
        return refid;
    }

    public void setRefid(String refid) {
        this.refid = refid;
    }

    public List<Ant_PathElement> getAnt_pathelements() {
        return ant_pathelements;
    }

    public void addAnt_pathelement(Ant_pathelement ant_pathelement) {
        this.ant_pathelements.add(ant_pathelement);
    }

}