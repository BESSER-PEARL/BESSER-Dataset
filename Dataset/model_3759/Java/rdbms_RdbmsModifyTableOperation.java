





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsModifyTableOperation extends RdbmsTableOperation {

    private String nameChanged;





    private rdbms_RdbmsTable rdbms_rdbmstable;


    public rdbms_RdbmsModifyTableOperation(
        String nameChanged    ) {
        super(
        );
        this.nameChanged = nameChanged;
    }


    public String getNamechanged() {
        return nameChanged;
    }

    public void setNamechanged(String nameChanged) {
        this.nameChanged = nameChanged;
    }

    public rdbms_RdbmsTable getRdbms_rdbmstable() {
        return rdbms_rdbmstable;
    }

    public void setRdbms_rdbmstable(rdbms_RdbmsTable rdbms_rdbmstable) {
        this.rdbms_rdbmstable = rdbms_rdbmstable;
    }

}