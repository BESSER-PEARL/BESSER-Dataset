





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsViewRecordValue  {

    private String value;





    private rdbms_RdbmsViewRecord rdbms_rdbmsviewrecord;




    private rdbms_RdbmsViewIdentifierField rdbms_rdbmsviewidentifierfield;




    private rdbms_RdbmsViewValueField rdbms_rdbmsviewvaluefield;


    public rdbms_RdbmsViewRecordValue(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public rdbms_RdbmsViewRecord getRdbms_rdbmsviewrecord() {
        return rdbms_rdbmsviewrecord;
    }

    public void setRdbms_rdbmsviewrecord(rdbms_RdbmsViewRecord rdbms_rdbmsviewrecord) {
        this.rdbms_rdbmsviewrecord = rdbms_rdbmsviewrecord;
    }
    public rdbms_RdbmsViewIdentifierField getRdbms_rdbmsviewidentifierfield() {
        return rdbms_rdbmsviewidentifierfield;
    }

    public void setRdbms_rdbmsviewidentifierfield(rdbms_RdbmsViewIdentifierField rdbms_rdbmsviewidentifierfield) {
        this.rdbms_rdbmsviewidentifierfield = rdbms_rdbmsviewidentifierfield;
    }
    public rdbms_RdbmsViewValueField getRdbms_rdbmsviewvaluefield() {
        return rdbms_rdbmsviewvaluefield;
    }

    public void setRdbms_rdbmsviewvaluefield(rdbms_RdbmsViewValueField rdbms_rdbmsviewvaluefield) {
        this.rdbms_rdbmsviewvaluefield = rdbms_rdbmsviewvaluefield;
    }

}