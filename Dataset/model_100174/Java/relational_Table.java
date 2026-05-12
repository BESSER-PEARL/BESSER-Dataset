





import java.util.List;
import java.util.ArrayList;

public class relational_Table extends ColumnSet {

    private int cardinality;
    private boolean materialized;
    private boolean supportsUpdate;
    private boolean system;



    public relational_Table(
        int cardinality,        boolean materialized,        boolean supportsUpdate,        boolean system    ) {
        super(
        );
        this.cardinality = cardinality;
        this.materialized = materialized;
        this.supportsUpdate = supportsUpdate;
        this.system = system;
    }


    public int getCardinality() {
        return cardinality;
    }

    public void setCardinality(int cardinality) {
        this.cardinality = cardinality;
    }
    public boolean getMaterialized() {
        return materialized;
    }

    public void setMaterialized(boolean materialized) {
        this.materialized = materialized;
    }
    public boolean getSupportsupdate() {
        return supportsUpdate;
    }

    public void setSupportsupdate(boolean supportsUpdate) {
        this.supportsUpdate = supportsUpdate;
    }
    public boolean getSystem() {
        return system;
    }

    public void setSystem(boolean system) {
        this.system = system;
    }


}