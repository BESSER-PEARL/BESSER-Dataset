





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_ClassPath extends Set {

    private String refid;





    private List<PathElement> pathelements;




    private List<FileSet> filesets;


    public MavenMaven_ClassPath(
        String refid    ) {
        super(
        );
        this.refid = refid;
        this.pathelements = new ArrayList<>();
        this.filesets = new ArrayList<>();
    }

    public MavenMaven_ClassPath(
        String refid        ArrayList<PathElement> pathelements,        ArrayList<FileSet> filesets    ) {
        this.refid = refid;
        this.pathelements = pathelements;
        this.filesets = filesets;
    }

    public String getRefid() {
        return refid;
    }

    public void setRefid(String refid) {
        this.refid = refid;
    }

    public List<PathElement> getPathelements() {
        return pathelements;
    }

    public void addPathelement(Pathelement pathelement) {
        this.pathelements.add(pathelement);
    }
    public List<FileSet> getFilesets() {
        return filesets;
    }

    public void addFileset(Fileset fileset) {
        this.filesets.add(fileset);
    }

}