





import java.util.List;
import java.util.ArrayList;

public class builds_ChangeSet  {

    private String kind;





    private builds_Build builds_build;


    public builds_ChangeSet(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public builds_Build getBuilds_build() {
        return builds_build;
    }

    public void setBuilds_build(builds_Build builds_build) {
        this.builds_build = builds_build;
    }

}