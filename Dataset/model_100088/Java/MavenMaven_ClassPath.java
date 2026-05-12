





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_ClassPath extends Set {

    private String refid;





    private List<MavenMaven_PathElement> mavenmaven_pathelements;


    public MavenMaven_ClassPath(
        String refid    ) {
        super(
        );
        this.refid = refid;
        this.mavenmaven_pathelements = new ArrayList<>();
    }

    public MavenMaven_ClassPath(
        String refid        ArrayList<MavenMaven_PathElement> mavenmaven_pathelements    ) {
        this.refid = refid;
        this.mavenmaven_pathelements = mavenmaven_pathelements;
    }

    public String getRefid() {
        return refid;
    }

    public void setRefid(String refid) {
        this.refid = refid;
    }

    public List<MavenMaven_PathElement> getMavenmaven_pathelements() {
        return mavenmaven_pathelements;
    }

    public void addMavenmaven_pathelement(Mavenmaven_pathelement mavenmaven_pathelement) {
        this.mavenmaven_pathelements.add(mavenmaven_pathelement);
    }

}