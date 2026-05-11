





import java.util.List;
import java.util.ArrayList;

public class persistence_AssociationWithoutContainment extends Association {

    private boolean targetUnique;
    private String targetCardinality;



    public persistence_AssociationWithoutContainment(
        boolean targetUnique,        String targetCardinality    ) {
        super(
        );
        this.targetUnique = targetUnique;
        this.targetCardinality = targetCardinality;
    }


    public boolean getTargetunique() {
        return targetUnique;
    }

    public void setTargetunique(boolean targetUnique) {
        this.targetUnique = targetUnique;
    }
    public String getTargetcardinality() {
        return targetCardinality;
    }

    public void setTargetcardinality(String targetCardinality) {
        this.targetCardinality = targetCardinality;
    }


}