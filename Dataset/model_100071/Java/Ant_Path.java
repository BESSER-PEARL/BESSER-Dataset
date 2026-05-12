





import java.util.List;
import java.util.ArrayList;

public class Ant_Path extends Set {

    private String id;
    private String refid;





    private Ant_Project ant_project;




    private Ant_Path ant_path;


    public Ant_Path(
        String id,        String refid    ) {
        super(
        );
        this.id = id;
        this.refid = refid;
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

    public Ant_Project getAnt_project() {
        return ant_project;
    }

    public void setAnt_project(Ant_Project ant_project) {
        this.ant_project = ant_project;
    }
    public Ant_Path getAnt_path() {
        return ant_path;
    }

    public void setAnt_path(Ant_Path ant_path) {
        this.ant_path = ant_path;
    }

}