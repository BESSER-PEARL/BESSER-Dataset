





import java.util.List;
import java.util.ArrayList;

public class rdbms_Table  {

    private String name;





    private rdbms_RDBMSModel rdbms_rdbmsmodel;


    public rdbms_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdbms_RDBMSModel getRdbms_rdbmsmodel() {
        return rdbms_rdbmsmodel;
    }

    public void setRdbms_rdbmsmodel(rdbms_RDBMSModel rdbms_rdbmsmodel) {
        this.rdbms_rdbmsmodel = rdbms_rdbmsmodel;
    }

}