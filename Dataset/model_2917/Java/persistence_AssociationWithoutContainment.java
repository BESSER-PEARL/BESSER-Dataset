





import java.util.List;
import java.util.ArrayList;

public class persistence_AssociationWithoutContainment extends EntityAssociation {

    private String targetCardinality;
    private boolean targetUnique;



    public persistence_AssociationWithoutContainment(
        String targetCardinality,        boolean targetUnique    ) {
        super(
        );
        this.targetCardinality = targetCardinality;
        this.targetUnique = targetUnique;
    }


    public String getTargetcardinality() {
        return targetCardinality;
    }

    public void setTargetcardinality(String targetCardinality) {
        this.targetCardinality = targetCardinality;
    }
    public boolean getTargetunique() {
        return targetUnique;
    }

    public void setTargetunique(boolean targetUnique) {
        this.targetUnique = targetUnique;
    }


}