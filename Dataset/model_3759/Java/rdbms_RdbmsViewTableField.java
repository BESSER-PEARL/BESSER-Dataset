





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsViewTableField extends RdbmsViewField {

    private boolean foreign;





    private rdbms_RdbmsField rdbms_rdbmsfield;


    public rdbms_RdbmsViewTableField(
        boolean foreign    ) {
        super(
        );
        this.foreign = foreign;
    }


    public boolean getForeign() {
        return foreign;
    }

    public void setForeign(boolean foreign) {
        this.foreign = foreign;
    }

    public rdbms_RdbmsField getRdbms_rdbmsfield() {
        return rdbms_rdbmsfield;
    }

    public void setRdbms_rdbmsfield(rdbms_RdbmsField rdbms_rdbmsfield) {
        this.rdbms_rdbmsfield = rdbms_rdbmsfield;
    }

}