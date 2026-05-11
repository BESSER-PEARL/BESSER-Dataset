





import java.util.List;
import java.util.ArrayList;

public class scxml_Anchor  {

    private String snapshot;
    private String type;





    private scxml_Parallel scxml_parallel;


    public scxml_Anchor(
        String snapshot,        String type    ) {
        this.snapshot = snapshot;
        this.type = type;
    }


    public String getSnapshot() {
        return snapshot;
    }

    public void setSnapshot(String snapshot) {
        this.snapshot = snapshot;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public scxml_Parallel getScxml_parallel() {
        return scxml_parallel;
    }

    public void setScxml_parallel(scxml_Parallel scxml_parallel) {
        this.scxml_parallel = scxml_parallel;
    }

}