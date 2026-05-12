





import java.util.List;
import java.util.ArrayList;

public class Ant_ClassPath extends Set {

    private String refid;





    private List<FileSet> filesets;




    private List<PathElement> pathelements;


    public Ant_ClassPath(
        String refid    ) {
        super(
        );
        this.refid = refid;
        this.filesets = new ArrayList<>();
        this.pathelements = new ArrayList<>();
    }

    public Ant_ClassPath(
        String refid        ArrayList<FileSet> filesets,        ArrayList<PathElement> pathelements    ) {
        this.refid = refid;
        this.filesets = filesets;
        this.pathelements = pathelements;
    }

    public String getRefid() {
        return refid;
    }

    public void setRefid(String refid) {
        this.refid = refid;
    }

    public List<FileSet> getFilesets() {
        return filesets;
    }

    public void addFileset(Fileset fileset) {
        this.filesets.add(fileset);
    }
    public List<PathElement> getPathelements() {
        return pathelements;
    }

    public void addPathelement(Pathelement pathelement) {
        this.pathelements.add(pathelement);
    }

}