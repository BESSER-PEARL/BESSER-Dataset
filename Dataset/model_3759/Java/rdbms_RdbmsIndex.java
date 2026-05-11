





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsIndex extends RdbmsElement {

    private boolean unique;





    private rdbms_RdbmsTable rdbms_rdbmstable;




    private rdbms_RdbmsTable rdbms_rdbmstable;


    public rdbms_RdbmsIndex(
        boolean unique    ) {
        super(
        );
        this.unique = unique;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }

    public rdbms_RdbmsTable getRdbms_rdbmstable() {
        return rdbms_rdbmstable;
    }

    public void setRdbms_rdbmstable(rdbms_RdbmsTable rdbms_rdbmstable) {
        this.rdbms_rdbmstable = rdbms_rdbmstable;
    }
    public rdbms_RdbmsTable getRdbms_rdbmstable() {
        return rdbms_rdbmstable;
    }

    public void setRdbms_rdbmstable(rdbms_RdbmsTable rdbms_rdbmstable) {
        this.rdbms_rdbmstable = rdbms_rdbmstable;
    }

}