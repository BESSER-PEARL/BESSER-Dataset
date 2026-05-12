





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Path extends Set {

    private String id;
    private String refid;





    private List<FileSet> filesets;




    private Path path;


    public MavenMaven_Path(
        String id,        String refid    ) {
        super(
        );
        this.id = id;
        this.refid = refid;
        this.filesets = new ArrayList<>();
    }

    public MavenMaven_Path(
        String id,        String refid        ArrayList<FileSet> filesets    ) {
        this.id = id;
        this.refid = refid;
        this.filesets = filesets;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }

}