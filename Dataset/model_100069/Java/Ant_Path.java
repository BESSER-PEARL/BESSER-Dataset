





import java.util.List;
import java.util.ArrayList;

public class Ant_Path extends Set {

    private String refid;
    private String id;





    private Path path;


    public Ant_Path(
        String refid,        String id    ) {
        super(
        );
        this.refid = refid;
        this.id = id;
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

    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }

}