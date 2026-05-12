





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_Index extends SQLObject {

    private int fillFactor;
    private boolean systemGenerated;
    private boolean clustered;
    private boolean unique;



    public sqlmodel_constraints_Index(
        int fillFactor,        boolean systemGenerated,        boolean clustered,        boolean unique    ) {
        super(
        );
        this.fillFactor = fillFactor;
        this.systemGenerated = systemGenerated;
        this.clustered = clustered;
        this.unique = unique;
    }


    public int getFillfactor() {
        return fillFactor;
    }

    public void setFillfactor(int fillFactor) {
        this.fillFactor = fillFactor;
    }
    public boolean getSystemgenerated() {
        return systemGenerated;
    }

    public void setSystemgenerated(boolean systemGenerated) {
        this.systemGenerated = systemGenerated;
    }
    public boolean getClustered() {
        return clustered;
    }

    public void setClustered(boolean clustered) {
        this.clustered = clustered;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}