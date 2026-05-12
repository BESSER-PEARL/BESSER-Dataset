





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_UniqueConstraint extends ReferenceConstraint {

    private boolean clustered;



    public sqlmodel_constraints_UniqueConstraint(
        boolean clustered    ) {
        super(
        );
        this.clustered = clustered;
    }


    public boolean getClustered() {
        return clustered;
    }

    public void setClustered(boolean clustered) {
        this.clustered = clustered;
    }


}