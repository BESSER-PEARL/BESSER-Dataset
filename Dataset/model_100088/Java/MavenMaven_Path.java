





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Path extends Set {

    private String refid;
    private String id;





    private MavenMaven_Path mavenmaven_path;




    private MavenMaven_Project mavenmaven_project;


    public MavenMaven_Path(
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

    public MavenMaven_Path getMavenmaven_path() {
        return mavenmaven_path;
    }

    public void setMavenmaven_path(MavenMaven_Path mavenmaven_path) {
        this.mavenmaven_path = mavenmaven_path;
    }
    public MavenMaven_Project getMavenmaven_project() {
        return mavenmaven_project;
    }

    public void setMavenmaven_project(MavenMaven_Project mavenmaven_project) {
        this.mavenmaven_project = mavenmaven_project;
    }

}