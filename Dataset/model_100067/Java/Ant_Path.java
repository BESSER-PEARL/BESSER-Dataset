





import java.util.List;
import java.util.ArrayList;

public class Ant_Path extends Set {

    private String refid;
    private String id;





    private List<FileSet> filesets;




    private Path path;




    private List<PathElement> pathelements;


    public Ant_Path(
        String refid,        String id    ) {
        super(
        );
        this.refid = refid;
        this.id = id;
        this.filesets = new ArrayList<>();
        this.pathelements = new ArrayList<>();
    }

    public Ant_Path(
        String refid,        String id        ArrayList<FileSet> filesets,        ArrayList<PathElement> pathelements    ) {
        this.refid = refid;
        this.id = id;
        this.filesets = filesets;
        this.pathelements = pathelements;
    }

    public String getRefid() {
        return refid;
    }

    public void setRefid(String refid) {
        this.refid = refid;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<FileSet> getFilesets() {
        return filesets;
    }

    public void addFileset(Fileset fileset) {
        this.filesets.add(fileset);
    }
    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }
    public List<PathElement> getPathelements() {
        return pathelements;
    }

    public void addPathelement(Pathelement pathelement) {
        this.pathelements.add(pathelement);
    }

}