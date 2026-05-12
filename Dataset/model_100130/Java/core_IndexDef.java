





import java.util.List;
import java.util.ArrayList;

public class core_IndexDef extends DatabaseObjectDef {

    private boolean unique;
    private boolean clustered;



    public core_IndexDef(
        boolean unique,        boolean clustered    ) {
        super(
        );
        this.unique = unique;
        this.clustered = clustered;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getClustered() {
        return clustered;
    }

    public void setClustered(boolean clustered) {
        this.clustered = clustered;
    }


}