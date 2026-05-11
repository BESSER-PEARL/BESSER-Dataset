





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsConfiguration  {

    private String dialect;





    private rdbms_RdbmsModel rdbms_rdbmsmodel;


    public rdbms_RdbmsConfiguration(
        String dialect    ) {
        this.dialect = dialect;
    }


    public String getDialect() {
        return dialect;
    }

    public void setDialect(String dialect) {
        this.dialect = dialect;
    }

    public rdbms_RdbmsModel getRdbms_rdbmsmodel() {
        return rdbms_rdbmsmodel;
    }

    public void setRdbms_rdbmsmodel(rdbms_RdbmsModel rdbms_rdbmsmodel) {
        this.rdbms_rdbmsmodel = rdbms_rdbmsmodel;
    }

}