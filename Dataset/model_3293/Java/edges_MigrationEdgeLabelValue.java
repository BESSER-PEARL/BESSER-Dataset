





import java.util.List;
import java.util.ArrayList;

public class edges_MigrationEdgeLabelValue extends LabelValue {

    private float migrationRate;



    public edges_MigrationEdgeLabelValue(
        float migrationRate    ) {
        super(
        );
        this.migrationRate = migrationRate;
    }


    public float getMigrationrate() {
        return migrationRate;
    }

    public void setMigrationrate(float migrationRate) {
        this.migrationRate = migrationRate;
    }


}